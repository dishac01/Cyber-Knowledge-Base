malicious_ips = [
    "192.168.1.100",
    "10.10.10.10"
]

ip = input("Enter IP: ")

if ip in malicious_ips:
    print("Malicious IP")
else:
    print("Safe IP")
