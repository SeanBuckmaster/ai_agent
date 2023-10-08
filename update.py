import os
import shutil

# Ensure to backup your project before running this script

# Directories to organize files
directories = {
    "BusinessLayer": ["ai_tasks.py", "ai_goals.py", "ai_errors.py"],
    "DataLayer": ["ai_data_read.py", "ai_data_write.py"],
    "PresentationLayer": ["ai_interface.py"],
    "CommonLayer": ["ai_xml_read.py", "ai_xml_write.py"]
}

# Create directories and move files
for dir_name, files in directories.items():
    os.makedirs(dir_name, exist_ok=True)
    for file_name in files:
        if os.path.exists(file_name):  # Check if file exists before moving
            shutil.move(file_name, os.path.join(dir_name, file_name))
        else:
            print(f"Warning: {file_name} does not exist and was not moved.")

# Initialize Git if not already done
if not os.path.exists(".git"):
    os.system('git init')

# Committing the changes to Git
os.system('git add .')
os.system('git commit -m "Refactoring: Organized files into layers"')

# Erasing the content of update.py after execution
with open("update.py", "w") as f:
    f.write("# This script has been executed and is now empty to prevent re-execution.\n")

print("Update completed! Files have been organized into respective directories.")
