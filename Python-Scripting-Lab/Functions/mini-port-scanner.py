import socket

def scan_port(ip, port):

    s = socket.socket()
    s.settimeout(1)

    result = s.connect_ex((ip, port))

    s.close()

    return result == 0

ip = input("IP: ")

for port in [21,22,80,443]:

    if scan_port(ip, port):
        print(f"{port} OPEN")
