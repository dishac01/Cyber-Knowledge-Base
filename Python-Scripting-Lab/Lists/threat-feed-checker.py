malicious_ips = [
    "10.10.10.10",
    "192.168.1.100"
]

network_ips = [
    "192.168.1.5",
    "10.10.10.10",
    "172.16.0.1"
]

for ip in network_ips:
    if ip in malicious_ips:
        print(f"ALERT: {ip}")
