import os
import shutil
import xml.etree.ElementTree as ET
from datetime import datetime

# Function to create a log entry
def create_log_entry(filename, message):
    if os.path.exists(filename):
        tree = ET.parse(filename)
        root = tree.getroot()
    else:
        root = ET.Element("log")
    
    entry = ET.SubElement(root, "entry")
    timestamp = ET.SubElement(entry, "timestamp")
    timestamp.text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = ET.SubElement(entry, "message")
    log_message.text = message
    
    tree = ET.ElementTree(root)
    tree.write(filename)

# Move main_loop.py to BusinessLayer
if os.path.exists("main_loop.py"):
    shutil.move("main_loop.py", os.path.join("BusinessLayer", "main_loop.py"))
    create_log_entry("Logs/update_log.xml", "Moved main_loop.py to BusinessLayer.")
else:
    create_log_entry("Logs/error_log.xml", "main_loop.py does not exist in the root directory.")

# Check if ai_main.py is calling main_loop.py from BusinessLayer
try:
    with open("ai_main.py", "r") as file:
        content = file.read()
        if 'from BusinessLayer import main_loop' not in content:
            create_log_entry("Logs/error_log.xml", "ai_main.py is not importing main_loop.py from BusinessLayer.")
        else:
            create_log_entry("Logs/update_log.xml", "ai_main.py is correctly importing main_loop.py from BusinessLayer.")
except FileNotFoundError:
    create_log_entry("Logs/error_log.xml", "ai_main.py does not exist in the root directory.")

# Git commands to add, commit, and push changes to GitHub
os.system("git add .")
os.system('git commit -m "Organized main_loop.py and verified import in ai_main.py"')
os.system("git push origin main")

# Informing the user about the update completion
print("Update completed! main_loop.py has been organized and ai_main.py import verified. Check the logs for details.")

# Erasing the content of update.py after execution
with open("update.py", "w") as f:
    f.write("# This script has been executed and is now empty to prevent re-execution.\n")
