import pyshark
import os

def run_sniffer(interface='eth0', packet_count=10):
    os.makedirs("reports", exist_ok=True)
    cap = pyshark.LiveCapture(interface=interface)
    print(f"[+] Capturing {packet_count} packets on {interface}...")
    cap.sniff(packet_count=packet_count)

    with open("reports/packet_capture.txt", "w") as f:
        for pkt in cap:
            f.write(str(pkt) + "\n")

    print("[+] Packet capture complete. Saved to reports/packet_capture.txt")
