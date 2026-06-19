import socket
import logging

logging.basicConfig(
    filename="scan.log",
    level=logging.INFO
)

target = input("Target IP: ")

for port in [21,22,23,80,443]:
    try:
        s = socket.socket()
        s.settimeout(1)

        result = s.connect_ex((target,port))

        if result == 0:
            print(f"Port {port} OPEN")
            logging.info(f"{target}:{port} OPEN")

        s.close()

    except Exception as err:
        logging.error(err)
