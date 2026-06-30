from pathlib import Path
import shutil
import zipfile

source = Path("computers")
evidence = Path("Evidence")

extensions = [
    ".log",
    ".txt",
    ".dmp",
    ".pcap",
    ".evtx"
]

evidence.mkdir(exist_ok=True)

for folder, subfolders, files in __import__("os").walk(source):

    folder = Path(folder)

    computer = folder.name

    for file in files:

        filepath = folder / file

        if filepath.suffix.lower() in extensions:

            new_name = f"{computer}_{file}"

            shutil.copy(
                filepath,
                evidence / new_name
            )

            print(f"Collected {new_name}")

with zipfile.ZipFile(
    "Evidence.zip",
    "w"
) as zip_file:

    for file in evidence.iterdir():

        zip_file.write(
            file,
            arcname=file.name
        )

print("Evidence.zip created successfully!")
