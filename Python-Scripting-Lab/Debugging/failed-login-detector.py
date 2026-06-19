import logging

logging.basicConfig(filename="alert.log", level=logging.INFO)

failed = 0

with open("logs.txt") as f:
    for line in f:
        if "Failed" in line:
            failed += 1

if failed >= 3:
    logging.warning("Multiple failed logins detected")
    print("ALERT!")
