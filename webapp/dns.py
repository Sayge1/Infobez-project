import subprocess


def set_dns(primary_dns, secondary_dns=None):
    result = subprocess.run(['netsh', 'interface', 'ipv4', 'show', 'interfaces'], capture_output=True, text=True)
    interfaces = result.stdout.splitlines()
    active_interface = None
    for line in interfaces:
        if "Connected" in line:
            active_interface = line.split()[-1]
            break
    if not active_interface:
        return

    if secondary_dns:
        subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'dns', f'name={active_interface}', 'static', primary_dns])
        subprocess.run(
            ['netsh', 'interface', 'ipv4', 'add', 'dns', f'name={active_interface}', secondary_dns, 'index=2'])
    else:
        subprocess.run(['netsh', 'interface', 'ipv4', 'set', 'dns', f'name={active_interface}', 'static', primary_dns])




set_dns("77.88.8.88")