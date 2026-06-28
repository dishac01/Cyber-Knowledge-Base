log1.txt
powershell.exe started
chrome.exe started
cmd.exe executed

log2.txt
User Login
Everything Normal
CVE-2023-23397 detected



from pathlib import Path

ioc_list = [
    "powershell.exe",
    "cmd.exe",
    "malware.exe",
    "ransomware",
    "CVE-"
]

log_folder = Path("logs")

report = []

for logfile in log_folder.glob("*.txt"):

    report.append(f"\n----- {logfile.name} -----")

    with open(logfile, "r") as file:

        content = file.read()

        found = False

        for ioc in ioc_list:

            if ioc.lower() in content.lower():

                report.append(f"Found IOC: {ioc}")

                found = True

        if not found:
            report.append("No IOC Found")

final_report = "\n".join(report)

print(final_report)

with open("ioc_report.txt", "w") as file:
    file.write(final_report)

print("\nReport Generated!")
