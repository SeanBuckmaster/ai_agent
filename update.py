# This script has been executed and is now empty to prevent re-execution.
import os
import shutil
import xml.etree.ElementTree as ET
from datetime import datetime

# Function to create a log entry in XML format
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

# Convert stop_flag.txt to XML and move to DataLayer
if os.path.exists("stop_flag.txt"):
    os.remove("stop_flag.txt")

stop_flag_root = ET.Element("stop_flag")
flag = ET.SubElement(stop_flag_root, "flag")
flag.text = "False"
tree = ET.ElementTree(stop_flag_root)
tree.write("DataLayer/stop_flag.xml")

# Move main_loop.py to BusinessLayer
if os.path.exists("main_loop.py"):
    shutil.move("main_loop.py", "BusinessLayer/main_loop.py")

# Git commands to add, commit, and push changes to GitHub
os.system("git add .")
os.system('git commit -m "Organized files and converted stop_flag to XML"')
os.system("git push origin main")

# Log the update
create_log_entry("Logs/update_log.xml", "Organized files and converted stop_flag to XML. Moved main_loop.py to BusinessLayer.")

# Informing the user about the update completion
print("Update completed! Files have been organized, stop_flag.txt has been converted to XML, and main_loop.py has been moved to BusinessLayer.")
