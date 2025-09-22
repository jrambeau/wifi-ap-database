#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Update AP Database Script
========================

This script automates the process of updating the AP database from Excel,
working across Windows, macOS, and Linux platforms.
"""

import os
import sys
import shutil
import subprocess
from datetime import datetime
from pathlib import Path
import colorama
from colorama import Fore, Style

# Fix Unicode output on Windows
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")
    os.environ["PYTHONIOENCODING"] = "utf-8"

# Initialize colorama for cross-platform colored output
colorama.init()

def print_color(message, color=Fore.WHITE, bold=False):
    """Print colored output that works on all platforms"""
    try:
        style = Style.BRIGHT if bold else ""
        print(f"{style}{color}{message}{Style.RESET_ALL}")
    except UnicodeEncodeError:
        # Fallback to plain text if Unicode fails
        plain_message = message.encode("ascii", "replace").decode()
        print(f"{style}{color}{plain_message}{Style.RESET_ALL}")

def run_command(command, error_message):
    """Run a shell command and handle errors"""
    try:
        # Create environment with UTF-8 encoding
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        
        # On Windows, use python.exe with proper encoding
        if sys.platform == "win32" and command.startswith("python "):
            python_exe = sys.executable
            command = f"\"{python_exe}\" {command[7:]}"
        
        result = subprocess.run(
            command,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
            encoding="utf-8",
            env=env,
            errors="replace"  # Replace invalid chars instead of failing
        )
        if result.stdout:
            # Clean up output if needed
            cleaned_output = result.stdout.encode("ascii", "replace").decode()
            print(cleaned_output)
        return True
    except subprocess.CalledProcessError as e:
        print_color(f"Error: {error_message}", Fore.RED)
        if e.stderr:
            # Clean up the error output
            stderr = e.stderr.encode("ascii", "replace").decode()
            print_color(f"Details: {stderr}", Fore.RED)
        return False

def create_backup(file_path, backup_dir):
    """Create a backup of a file with timestamp"""
    if not os.path.exists(file_path):
        return
    
    # Create backup directory if it doesn"t exist
    os.makedirs(backup_dir, exist_ok=True)
    
    # Generate backup filename with timestamp
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_name = f"{Path(file_path).name}.backup_{timestamp}"
    backup_path = os.path.join(backup_dir, backup_name)
    
    # Create the backup
    shutil.copy2(file_path, backup_path)
    print_color(f"Created backup: {backup_path}", Fore.CYAN)

def check_git_changes():
    """Check if there are changes to commit"""
    result = subprocess.run(
        "git status --porcelain",
        shell=True,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace"
    )
    return bool(result.stdout.strip())

def update_database():
    """Main function to update the AP database"""
    print_color("Starting AP Database Update Process...", Fore.GREEN, bold=True)
    print_color("=============================================", Fore.GREEN)
    
    # 1. Create backups
    print_color("\nCreating backups...", Fore.CYAN)
    backup_dir = "backups"
    create_backup("wifi-ap-database.xlsx", backup_dir)
    create_backup("index.md", backup_dir)
    create_backup(os.path.join("_data", "ap_models.yaml"), backup_dir)
    
    # 2. Update YAML data
    print_color("\nUpdating YAML data...", Fore.CYAN)
    if not run_command(
        f"{sys.executable} convert_excel_to_yaml.py --excel wifi-ap-database.xlsx --no-backup",
        "Error updating YAML data. Please check the Excel file and try again."
    ):
        return False
    
    # 3. Update table structure
    print_color("\nUpdating table structure...", Fore.CYAN)
    if not run_command(
        f"{sys.executable} update_table_only.py",
        "Error updating table structure. Please check the files and try again."
    ):
        return False
    
    # 4. Git operations
    print_color("\nChecking Git status...", Fore.CYAN)
    if check_git_changes():
        print_color("Changes detected. Proceeding with commit...", Fore.YELLOW)
        
        # Stage the changes
        if not run_command(
            "git add _data/ap_models.yaml index.md",
            "Error staging files."
        ):
            return False
        
        # Commit with current date
        commit_date = datetime.now().strftime("%Y-%m-%d %H:%M")
        if not run_command(
            f"git commit -m \"Update AP database - {commit_date}\"",
            "Error committing changes."
        ):
            return False
        
        # Push to GitHub
        print_color("\nPushing changes to GitHub...", Fore.CYAN)
        if not run_command(
            "git push origin main",
            "Error pushing changes to GitHub. Please check your connection and try again."
        ):
            return False
        
        print_color("\nSuccessfully updated and deployed AP database!", Fore.GREEN)
        print_color("The website will be updated in a few minutes.", Fore.YELLOW)
    else:
        print_color("\nNo changes detected in the database.", Fore.YELLOW)
    
    return True

def check_requirements():
    """Check if all required files and tools are available"""
    required_files = [
        "wifi-ap-database.xlsx",
        "convert_excel_to_yaml.py",
        "update_table_only.py"
    ]
    
    missing_files = []
    for file in required_files:
        if not os.path.exists(file):
            missing_files.append(file)
    
    if missing_files:
        print_color("Missing required files:", Fore.RED)
        for file in missing_files:
            print_color(f"   - {file}", Fore.RED)
        return False
    
    # Check if git is available
    try:
        subprocess.run(
            "git --version",
            shell=True,
            check=True,
            capture_output=True,
            encoding="utf-8",
            errors="replace"
        )
    except subprocess.CalledProcessError:
        print_color("Git is not installed or not available in PATH", Fore.RED)
        return False
    
    return True

def main():
    """Main entry point"""
    try:
        # Change to script directory
        os.chdir(os.path.dirname(os.path.abspath(__file__)))
        
        # Check requirements
        if not check_requirements():
            sys.exit(1)
        
        # Run the update process
        if not update_database():
            sys.exit(1)
        
    except KeyboardInterrupt:
        print_color("\n\nUpdate process interrupted by user.", Fore.YELLOW)
        sys.exit(1)
    except Exception as e:
        print_color(f"\nUnexpected error: {e}", Fore.RED)
        sys.exit(1)

if __name__ == "__main__":
    main()
