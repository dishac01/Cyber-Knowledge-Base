from pathlib import Path

folder = Path("files")

report = []

report.append("======= File Report =======\n")

for file in folder.glob("*"):

    report.append(f"Name      : {file.name}")
    report.append(f"Extension : {file.suffix}")
    report.append(f"Size      : {file.stat().st_size} bytes")
    report.append(f"Path      : {file.resolve()}")
    report.append("-" * 40)

output = "\n".join(report)

print(output)

with open("file_report.txt", "w") as file:
    file.write(output)

print("\nReport saved!")
