# Firewall Backup & Policy Audit

This tool connects to a Cisco ASA firewall, backs up the running configuration, and performs a simple ACL count audit.

## Features

- Uses Netmiko to SSH into the ASA.
- Backs up running config to a timestamped file.
- Counts the number of `access-list` entries for a quick policy size audit.

## Prerequisites

- Python 3.x
- `pip install -r requirements.txt`
- Update `devices.yml` with firewall IP and credentials.

## How to Run

1. `python3 backup_and_audit.py`
2. Check the backup file for stored configuration.
3. Terminal output shows the number of ACL entries.
