# SSH-Discovery
SSH Discovery & Credential Auditor
A streamlined Python utility for identifying active SSH services and performing automated credential validation.

🔹 Key Features
Pre-Flight Checks: Performs ICMP pings and Scapy-based TCP SYN scanning to ensure the target is live and port 22 is open.

Flexible Wordlists:

Fixed User: Target a specific user with a list of potential passwords.

Combined Lists: Process username:password files using any custom separator (e.g., :, ;, or spaces).

Visual Feedback: Uses ANSI color-coded output for clear "SUCCESS" vs. "FAILED" status updates.

Verbose Logging: Optional -v flag to track every login attempt in real-time.

🔹 Technical Overview
The script follows a 3-step validation pipeline:

ICMP Ping: Confirms the host is online.

TCP SYN Scan: Confirms the SSH service is actually reachable.

SSH Handshake: Attempts authentication using the Paramiko library, handling exceptions to ensure the script continues running through the wordlist.

🔹 Installation & Usage
Bash
# Clone the repository
git clone https://github.com/yourusername/ssh-auditor.git

# Install dependencies
pip install scapy paramiko

# Example: Run an audit with a combined wordlist
python account_discovery.py -t 192.168.1.1 -D credentials.txt -s : -v
