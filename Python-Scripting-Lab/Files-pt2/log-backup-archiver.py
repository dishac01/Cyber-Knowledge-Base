from pathlib import Path
import shutil
import zipfile

source_folder = Path("logs")
backup_folder = Path("logs_backup")
zip_name = "logs_backup.zip"

# Remove old backup folder if it exists
if backup_folder.exists():
    shutil.rmtree(backup_folder)

# Copy entire folder
shutil.copytree(source_folder, backup_folder)

print("Logs copied successfully!")

# Create ZIP archive
with zipfile.ZipFile(zip_name, "w") as zip_file:

    for file in backup_folder.rglob("*"):

        if file.is_file():

            zip_file.write(
                file,
                arcname=file.relative_to(backup_folder)
            )

print(f"Archive created: {zip_name}")
