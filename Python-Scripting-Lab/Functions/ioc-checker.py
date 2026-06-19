def check_ioc(filename):

    iocs = [
        "malware.exe",
        "virus.dll",
        "bad.exe"
    ]

    return filename in iocs

file = input()

if check_ioc(file):
    print("Threat Found")
else:
    print("Safe")
