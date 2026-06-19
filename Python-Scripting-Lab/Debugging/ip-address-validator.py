import ipaddress
import logging

logging.basicConfig(filename="ip_validator.log", level=logging.INFO)

try:
    ip = input("Enter IP: ")
    ipaddress.ip_address(ip)

    logging.info(f"Valid IP: {ip}")
    print("Valid IP")

except Exception as err:
    logging.error(f"Invalid IP: {ip}")
    print(err)
