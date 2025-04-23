import platform
import os
import subprocess
import datetime
import sys

def error_hook(exctype, value, traceback):
	print("[!] Unhandled error:", value)

sys.excpthook = error_hook

def run_command(cmd):
    return subprocess.getoutput(cmd)

def get_basic_info():
    return {
        "Date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "OS": platform.system(),
        "OS Version": platform.version(),
        "Hostname": platform.node(),
        "Architecture": platform.machine(),
        "Kernel": run_command("uname -r")
    }

def get_users():
    return run_command("who")

def get_uptime():
    return run_command("uptime -p")

def get_disk_usage():
    return run_command("df -h")

def get_network_info():
    return run_command("ip a")

def get_open_ports():
    return run_command("ss -tuln")

def write_report(data: dict, filename="output/report.txt"):
    os.makedirs("output", exist_ok=True)
    with open(filename, "w") as f:
        for section, content in data.items():
            f.write(f"\n===== {section} =====\n")
            f.write(content if isinstance(content, str) else "\n".join(f"{k}:{v}" for k, v in content.items()))
            f.write("\n")

def main():
    print("[*] Runnimg Linux Enumeration...")

    report = {
        "System info": get_basic_info(),
        "Logged-in users": get_users(),
        "System Uptime": get_uptime(),
        "Disk Usage": get_disk_usage(),
        "Network Interfaces": get_network_info(),
        "Open Ports": get_open_ports()
    }

    write_report(report)
    print("[+] Report saved to output/report.txt")
    
    
if __name__ == "__main__":
        main()
