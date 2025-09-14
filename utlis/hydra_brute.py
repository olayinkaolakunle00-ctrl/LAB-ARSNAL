import subprocess
import os

def run_hydra(target_ip, user, wordlist):
    os.makedirs("reports", exist_ok=True)
    out_file = "reports/hydra_output.txt"
    cmd = ["hydra", "-l", user, "-P", wordlist, target_ip, "ftp", "-o", out_file]
    subprocess.run(cmd)
    print(f"[+] Hydra brute force complete. Saved to {out_file}")
