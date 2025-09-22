# Python Backup Automation Script

## Lab Overview
Created my first Python automation script to backup files, demonstrating programming fundamentals and practical automation skills for cybersecurity applications.

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
