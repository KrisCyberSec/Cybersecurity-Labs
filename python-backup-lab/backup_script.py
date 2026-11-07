# Reconstructed from my September 2025 lab screenshots (see README).
# The original file was lost when I changed macOS accounts.
import os
import shutil
from datetime import datetime


# Simple function to create backup folder
def make_backup_folder():
    now = datetime.now()
    folder_name = "backup_" + now.strftime("%Y%m%d_%H%M%S")
    try:
        os.mkdir(folder_name)
        print("Created backup folder:", folder_name)
        return folder_name
    except:
        print("Could not create folder")
        return None


def copy_file(source, destination_folder):
    try:
        # Copy the file
        shutil.copy(source, destination_folder)
        print("Copied:", source)
        return True
    except:
        print("Failed to copy:", source)
        return False

# Main part of the script
print("Starting my backup script...")

# Create backup folder
backup_folder = make_backup_folder()

if backup_folder:
    # List of files I want to backup
    files_to_backup = [
        os.path.expanduser("~/Desktop/test_file.txt")
    ]

    # Keep track of results
    successful = 0
    failed = 0

    # Try to backup each file
    for file_path in files_to_backup:
        if os.path.exists(file_path):
            if copy_file(file_path, backup_folder):
                successful += 1
            else:
                failed += 1
        else:
            print("File not found:", file_path)
            failed += 1

    # Show results
    print("\nBackup complete!")
    print("Successful:", successful)
    print("Failed:", failed)
else:
    print("Cannot continue without backup folder")
