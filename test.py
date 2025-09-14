import os

def test_reports_exist():
    files = [
        "nmap_report.txt",
        "hydra_output.txt",
        "packet_capture.txt",
        "metasploit_result.txt"
    ]
    missing = [f for f in files if not os.path.exists(f"reports/{f}")]
    assert not missing, f"Missing reports: {missing}"

if __name__ == "__main__":
    test_reports_exist()
    print("[✓] All report files exist.")
