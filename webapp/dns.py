import subprocess
from dns_interface import get_active_interface
def set_dns(active_interfaces):
    primary_dns = "77.88.8.8"
    for interface in active_interfaces:
        result = subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'dns', interface, 'static', primary_dns])

