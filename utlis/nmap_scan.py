import nmap
import os

def run_nmap(target_ip):
    scanner = nmap.PortScanner()
    
    print(f"[+] Starting Nmap scan on {target_ip}...")
    try:
        scanner.scan(hosts=target_ip, arguments='-sV')
    except Exception as e:
        print(f"[-] Nmap scan failed: {e}")
        return

    result = f"Scan results for {target_ip}\n\n"
    for host in scanner.all_hosts():
        result += f"Host: {host} ({scanner[host].hostname()})\n"
        result += f"State: {scanner[host].state()}\n"
        for proto in scanner[host].all_protocols():
            result += f"\nProtocol: {proto}\n"
            ports = scanner[host][proto].keys()
            for port in sorted(ports):
                port_info = scanner[host][proto][port]
                result += f"  Port: {port}  State: {port_info['state']}  Service: {port_info['name']}\n"

    # Save report
    os.makedirs("reports", exist_ok=True)
    output_file = f"reports/nmap_report.txt"
    with open(output_file, "w") as f:
        f.write(result)

    print(f"[✓] Nmap scan completed. Report saved to {output_file}")
