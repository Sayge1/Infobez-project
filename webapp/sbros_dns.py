import subprocess
from dns_interface import get_active_interface

def sbros_dns(active_interfaces):
    for interface in active_interfaces:
        try:
            subprocess.run(
                f'netsh interface ip set dnsservers name="{interface}" source=dhcp',
                check=True)
        except:
            pass
