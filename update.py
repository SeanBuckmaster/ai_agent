import os
import shutil

# Ensure to backup your project before running this script

# Directories and files to organize and create
directories = {
    "BusinessLayer": ["ai_tasks.py", "ai_goals.py", "ai_errors.py"],
    "DataLayer": ["ai_data_read.py", "ai_data_write.py"],
    "PresentationLayer": ["ai_interface.py"],
    "CommonLayer": ["ai_xml_read.py", "ai_xml_write.py"]
}

# Basic template for Python files
python_template = """\"\"\"
This is a template Python file for the AI Agent project.
\"\"\"

def main():
    pass

if __name__ == "__main__":
    main()
"""

# Create directories and files
for dir_name, files in directories.items():
    os.makedirs(dir_name, exist_ok=True)
    for file_name in files:
        file_path = os.path.join(dir_name, file_name)
        # Create file with basic template if it does not exist
        if not os.path.exists(file_path):
            with open(file_path, "w") as f:
                f.write(python_template)
            print(f"Created: {file_path}")
        else:
            print(f"Exists: {file_path}")

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
