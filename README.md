# Linux Enum Tool 🐧

A basic Linux system enumeration script written in Python.

This script collects:

- System info (kernel, architecture, OS)
- Logged-in users
- System uptime
- Disk usage
- Network interfaces
- Open ports

📁 Output is saved to: `output/report.txt`

## 💻 Usage

```bash
python3 linux_enum.py
```
⚙️ Requirements
Python 3

psutil (pip3 install psutil)

Tested on Ubuntu 20.04 / 22.04

📚 Why I Built This
As an ethical hacking student, I wanted to automate the first steps of post-exploitation recon. This script was built to reinforce my Linux + Python skills while learning how to gather system intelligence quickly.

🚀 Built by toxictager