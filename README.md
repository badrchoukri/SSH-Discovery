# SSH-Discovery
# SH-Auditor 🔐  
**Network Recon & Authentication Auditing Tool**

SH-Auditor is a high‑performance Python utility designed for **security auditing and network discovery**.  
It automates host discovery, SSH service detection, and credential validation with flexible wordlist support.

> ⚠️ **For educational and authorized security testing only.**

---

## 🚀 Features

- **Host Discovery**  
  Uses ICMP (Ping) to verify target availability before scanning.

- **Stealth SSH Scanning**  
  Leverages **Scapy TCP SYN scans** to detect open SSH ports without completing a full TCP handshake.

- **Automated Brute‑Force Testing**  
  Multi‑threaded authentication attempts using **Paramiko (SSHv2)**.

- **Dynamic Credential Parsing**  
  Supports multiple wordlist formats:
  - **Single User Mode**
    ```bash
    -u root -p passwords.txt
    ```
  - **Combined User:Password Mode**
    ```bash
    -D combo.txt -s :
    ```
    (Separator can be any character)

- **Colorized Terminal Output**  
  Clean ANSI‑colored feedback for:
  - Successful logins
  - Failed attempts
  - Host / port status

---

## 🛠️ Technical Stack

| Tool        | Purpose                                  |
|------------|------------------------------------------|
| Python 3   | Core logic                               |
| Scapy      | Packet crafting & TCP SYN scanning       |
| Paramiko   | SSHv2 protocol & authentication          |
| Subprocess | System‑level network checks              |

---

## 📦 Installation

```bash
pip install scapy paramiko
in attempt in real-time.

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
```bash
pip install scapy paramiko
```
# Example: Run an audit with a combined wordlist
```bash
python account_discovery.py -t 192.168.1.1 -D credentials.txt -s : -v
```
