# Python Backup Automation Script

## Lab Overview

The write-up describes a first Python script for copying files into a timestamped folder. What git actually contains is this README and six terminal screenshots. `backup_script.py` is not committed.

The screenshots show a Mac terminal. One of them is a home-directory listing. Account names and home paths stay in those images and are not repeated here.

## Evidence in this folder

| File | What the image shows |
| --- | --- |
| [01-clean-directory.png](01-clean-directory.png) | A terminal prompt after login on 2025-09-17. No directory listing in the frame. |
| [02-script-development.png](02-script-development.png) | nano (UW PICO 5.09) open on `backup_script.py`. The visible buffer has `copy_file` and the main loop. Imports and `make_backup_folder` are not in the frame. |
| [03-test-file-creation.png](03-test-file-creation.png) | A 55-byte Desktop test file created on 2025-09-18 at 14:40. |
| [04-script-execution.png](04-script-execution.png) | `python3 backup_script.py` printing `backup_20250918_144111`, one copied file, `Successful: 1`, `Failed: 0`. |
| [06-backup-validation.png](06-backup-validation.png) | `ls backup*` showing `backup_script.py` and `test_file.txt` inside `backup_20250918_144111`. |
| [5-results-verification.png](5-results-verification.png) | A home-directory listing that includes the backup folder from the run. |

There is no `05-` screenshot. The file names were left unchanged.

## Learning Objectives
- Learn Python programming basics
- Understand file system operations
- Practice error handling concepts
- Build practical automation tools

## Tools Used
- **Python 3** - Programming language
- **macOS Terminal** - Development environment
- **Nano** - Text editor for script development
- **Built-in Python libraries**: os, shutil, datetime

## Methodology

### 1. Script Development Process
- Started with basic Python script structure
- Added simple functions for folder creation and file copying
- Implemented basic error handling with try/except blocks
- Used clear variable names and comments for learning

### 2. Key Programming Concepts Applied
- **Functions**: Created `make_backup_folder()` and `copy_file()` functions
- **Variables**: Used descriptive names like `backup_folder` and `files_to_backup`
- **Loops**: Implemented for loop to process multiple files
- **Conditionals**: Used if/else statements for error checking
- **Exception Handling**: Added try/except blocks for robust operation

### 3. File Operations Implementation
- Used `os.mkdir()` to create directories
- Applied `shutil.copy()` for file copying operations
- Implemented `os.path.exists()` to check file availability
- Used `datetime.now()` for timestamp generation

### 4. Testing and Validation
- Created test file for backup demonstration
- Ran script multiple times to verify functionality
- Checked backup folder contents to confirm file copying
- Verified error handling with non-existent files

The six committed screenshots show one successful run on 2025-09-18 (`Successful: 1`, `Failed: 0`) and the folder listing after it. They do not show a second run or a missing-file failure.

## Script Functionality

### Core Features
- **Timestamped Backup Folders**: Creates folders with date/time stamps
- **File Validation**: Checks if files exist before attempting backup
- **Error Reporting**: Shows clear success/failure messages
- **Result Summary**: Displays count of successful and failed operations

### Sample Code Structure
```python
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
```

The block above is the excerpt stored in this file. It is not a complete script: the fence was unclosed in git, and the rest of `backup_script.py` was never committed. The editor screenshot shows a later part of the file, including a bare `except:` in `copy_file`. That bare handler is visible in the screenshot; it is not a pattern to copy into other tools.
