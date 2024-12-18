import yaml
from netmiko import ConnectHandler
from datetime import datetime

with open('devices.yml') as f:
    data = yaml.safe_load(f)

for fw in data['firewalls']:
    conn = ConnectHandler(**fw)
    hostname = conn.send_command("show run | include hostname").split()[1]
    running_config = conn.send_command("show run")
    conn.disconnect()

    # Save the backup
    now = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f"{hostname}_backup_{now}.cfg"
    with open(backup_file, 'w') as bf:
        bf.write(running_config)
    print(f"Backup saved to {backup_file}")

    # Simple audit: count ACL lines
    acl_lines = [line for line in running_config.splitlines() if line.strip().startswith('access-list')]
    print(f"{hostname} has {len(acl_lines)} ACL entries.")
