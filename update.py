# This script has been executed and is now empty to prevent re-execution.
import os

# Ensure to backup your project before running this script

# Directories to organize files
directories = {
    "VoiceCommands": [],
    "TaskManagement": ["ai_tasks.py", "ai_goals.py"],
    "UserInteraction": ["ai_interface.py"],
    "APIInteraction": ["ai_chatgpt.py"],
    "DataManagement": ["ai_data_read.py", "ai_data_write.py"],
    "ErrorHandling": ["ai_errors.py"],
    "Logging": [],
    "Testing": [],
    "Documentation": []
}

# Create directories and move files
for dir_name, files in directories.items():
    os.makedirs(dir_name, exist_ok=True)
    for file_name in files:
        if os.path.exists(file_name):
            os.rename(file_name, os.path.join(dir_name, file_name))
        else:
            print(f"Warning: {file_name} does not exist and was not moved.")

# Initialize Git if not already done
if not os.path.exists(".git"):
    os.system('git init')

# Committing the changes to Git
os.system('git add .')
os.system('git commit -m "Refactoring: Organized files into modules"')

# Erasing the content of update.py after execution
with open("update.py", "w") as f:
    f.write("# This script has been executed and is now empty to prevent re-execution.\n")

print("Update completed! Files have been organized into respective modules.")
