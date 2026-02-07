# SSH-Discovery  
**Network Recon & Authentication Auditing Tool**

SSH-Discovery is a high‑performance Python utility designed for **security auditing and network discovery**.  
It automates host discovery, SSH service detection, and credential validation with flexible wordlist support.

---

##  Features

- **Host Discovery**  
  Uses ICMP (Ping) to verify target availability before scanning.

- **Stealth SSH Scanning**  
  Leverages **Scapy TCP SYN scans** to detect open SSH ports without completing a full TCP handshake.

- **Automated SSH Brute‑Force Testing**  
  Multi‑threaded authentication attempts using **Paramiko (SSHv2)**.

- **Dynamic Credential Parsing**  
  Supports multiple wordlist formats:
  - **Single User Mode**
    ```bash
    -u root -p passwords.txt
    ```
  - **Combined User:Password Mode**
    ```bash
    -D combo.txt -s 
    ```
    (Separator can be any character)

---

## Technical Stack

| Tool        | Purpose                                  |
|------------|------------------------------------------|
| Python 3   | Core logic                               |
| Scapy      | Packet crafting & TCP SYN scanning       |
| Paramiko   | SSHv2 protocol & authentication          |
| Subprocess | System‑level network checks              |

---
Usage Examples
- Audit with a fixed username and password list
python account_discovery.py -t 192.168.1.100 -u admin -p rockyou.txt -v

- Audit using a combined user:password file
python account_discovery.py -t 192.168.1.100 -D users_pass.txt -s :

## Arguments Overview

| option        | Purpose                                  |
|---------------|------------------------------------------|
| -t            | Target IP address                        |
| -p            | Password wordlist                        |
| -u            | Fixed username                           |
| -D            | Combined user:pass file                  |
| -v            | Username/password separator              |
| -s            | Verbose output                           |

## install the script

```bash
git clone https://github.com/badrchoukri/SSH-Discovery.git
```

### Install Dependencies

```bash
pip install scapy paramiko
```

