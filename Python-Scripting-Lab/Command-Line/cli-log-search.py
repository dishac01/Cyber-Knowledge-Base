import sys
from pathlib import Path

# Check command-line arguments
if len(sys.argv) != 3:
    print("Usage: python cli_log_search.py <folder> <keyword>")
    sys.exit()

folder = Path(sys.argv[1])
keyword = sys.argv[2]

# Check folder exists
if not folder.exists():
    print("Folder not found!")
    sys.exit()

print(f"\nSearching '{keyword}' in {folder}...\n")

found = False

# Search every .log file
for logfile in folder.glob("*.log"):

    with open(logfile, "r") as file:

        for line_number, line in enumerate(file, start=1):

            if keyword.lower() in line.lower():

                print(f"{logfile.name}")
                print(f"Line {line_number}: {line.strip()}\n")

                found = True

if not found:
    print("No matching entries found.")
