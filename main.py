from utils import nmap_scan, hydra_brute, tshark_sniff, metasploit_exploit

target_ip = input("Enter target IP: ")

print("\n[1] Running Nmap...")
nmap_scan.run_nmap(target_ip)

print("\n[2] Running Hydra FTP Brute Force...")
hydra_brute.run_hydra(target_ip, user="admin", wordlist="/usr/share/wordlists/rockyou.txt")

print("\n[3] Running Packet Capture...")
tshark_sniff.run_sniffer(interface="eth0", packet_count=10)

print("\n[4] Running Metasploit Exploit...")
metasploit_exploit.run_exploit(rhost=target_ip, password='yourpassword')

print("\n[✓] All tasks completed. Check the 'reports/' directory.")
