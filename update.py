import os
import logging
import shutil

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.FileHandler("Logs/execution.log", 'a', 'utf-8'),
                              logging.StreamHandler()])

# Directories to organize files
directories = {
    "BusinessLayer": ["ai_task_processor.py"],
    "CommonLayer": ["ai_error_handler.py", "ai_xml_handler.py"]
}

# Create directories and move files
for dir_name, files in directories.items():
    os.makedirs(dir_name, exist_ok=True)
    for file_name in files:
        try:
            shutil.move(file_name, os.path.join(dir_name, file_name))
            logging.info(f"Moved {file_name} to {dir_name}")
        except FileNotFoundError:
            logging.warning(f"{file_name} does not exist and was not moved.")

# Committing the changes to Git
os.system('git add .')
os.system(f'git commit -m "Refactoring: Organized files into layers and added execution log"')
os.system('git push')

# Erasing the content of update.py after execution
with open("update.py", "w") as f:
    f.write("# This script has been executed and is now empty to prevent re-execution.\n")

logging.info("Update completed! Files have been organized into respective directories.")
