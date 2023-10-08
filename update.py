# update.py

import os
import shutil

# Ensure to backup your project before running this script

# Creating main_loop.py with the main loop function
main_loop_code = """
import time
import threading

def main_loop(task_processor_func):
    try:
        print("|/", end="", flush=True)
        while True:
            # Your main loop code here
            # ...
            # Call the task processor function
            task_processor_func()
            time.sleep(1)
            print("\\r|", end="", flush=True)
            time.sleep(1)
            print("\\r/", end="", flush=True)
    except KeyboardInterrupt:
        print("\\nStopping AI Main...")
"""

with open("main_loop.py", "w") as file:
    file.write(main_loop_code)

# Creating task_processor.py with a placeholder function for task processing
task_processor_code = """
def process_tasks():
    # Placeholder for task processing logic
    pass
"""

with open("task_processor.py", "w") as file:
    file.write(task_processor_code)

# Modifying ai_main.py to utilize main_loop and task_processor
ai_main_code = """
from main_loop import main_loop
from task_processor import process_tasks

# Calling the main loop function with the task processor function as an argument
main_loop(process_tasks)
"""

with open("ai_main.py", "w") as file:
    file.write(ai_main_code)

# Organizing files into respective directories
# Note: Adjust the file names and directory names as per your project structure
directories = {
    "BusinessLayer": ["ai_task_processor.py", "ai_tasks.xml", "ai_goals.py", "ai_errors.py"],
    "DataLayer": ["ai_data_read.py", "ai_data_write.py", "ai_error.xml", "ai_task.txt", "ai_tasks.xml", "goals.xml", "metrics.xml", "q_and_a.xml", "questions.xml", "turk.xml"],
    "PresentationLayer": ["ai_interface.py"],
    "CommonLayer": ["ai_xml_read.py", "ai_xml_write.py", "ai_chatgpt.py", "ai_error_handler.py", "ai_xml_handler.py"]
}

# Move files to their respective directories
for dir_name, files in directories.items():
    os.makedirs(dir_name, exist_ok=True)
    for file_name in files:
        if os.path.exists(file_name):
            shutil.move(file_name, os.path.join(dir_name, file_name))
        else:
            print(f"Warning: {file_name} does not exist and was not moved.")

# Git commands to add, commit, and push changes to GitHub
os.system("git add .")
os.system('git commit -m "Refactoring: Organized files and created main_loop.py and task_processor.py"')
os.system("git push origin main")

# Informing the user about the update completion
print("Update completed! Files have been organized, and main_loop.py and task_processor.py have been created and utilized in ai_main.py.")
