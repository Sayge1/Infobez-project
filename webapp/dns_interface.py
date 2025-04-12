import subprocess

def get_active_interface():
    active_interfaces = []
    result = subprocess.run(
        ["netsh", "interface", "show", "interface"],
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    if result.returncode != 0:
        raise Exception("Не удалось получить список сетевых интерфейсов.")

    for line in result.stdout.splitlines():
        if "Connected" in line or "Подключен" in line:
            parts = line.split()
            if len(parts) > 3:
                active_interfaces.append(parts[-1])
                active_interfaces.append(parts[-2] + " " + parts[-1])
                active_interfaces.append(parts[-3] + " " + parts[-2] + " " + parts[-1])
    return active_interfaces
