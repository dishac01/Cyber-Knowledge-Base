sample.log
INFO User logged in
ERROR Invalid password
INFO User logged out
WARNING Multiple failed logins
ERROR Database connection failed
CRITICAL Server Down
INFO Scan Complete


from pathlib import Path

log_file = Path("sample.log")

if not log_file.exists():
    print("Log file not found!")
    exit()

with open(log_file, "r") as file:
    logs = file.readlines()

info = 0
warning = 0
error = 0
critical = 0

for line in logs:

    if "INFO" in line:
        info += 1

    elif "WARNING" in line:
        warning += 1

    elif "ERROR" in line:
        error += 1

    elif "CRITICAL" in line:
        critical += 1

report = f"""
========= Security Report =========

Total Lines : {len(logs)}

INFO      : {info}
WARNING   : {warning}
ERROR     : {error}
CRITICAL  : {critical}
"""

print(report)

with open("security_report.txt", "w") as file:
    file.write(report)

print("Report saved as security_report.txt")
