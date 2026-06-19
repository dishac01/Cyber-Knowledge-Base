iocs = [
    "malware.exe",
    "bad.exe",
    "virus.dll"
]

files = [
    "chrome.exe",
    "bad.exe",
    "explorer.exe"
]

for file in files:
    if file in iocs:
        print(f"ALERT: {file} detected")
