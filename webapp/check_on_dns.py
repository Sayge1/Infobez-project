import subprocess

def check_on_dns():
    result = subprocess.run(
        ["netsh", "interface", "ipv4", "show", "dnsservers"],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )
    for line in result.stdout.splitlines():
        if "77.88.8.8" in line:
            return True
    return False
