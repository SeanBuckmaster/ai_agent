import os
import xml.etree.ElementTree as ET
from datetime import datetime

# Delete old log files if they exist
if os.path.exists("Logs/update_log.xml"):
    os.remove("Logs/update_log.xml")

if os.path.exists("Logs/error_log.xml"):
    os.remove("Logs/error_log.xml")

# Create a new XML log file with a timestamp and a log entry
def create_log_entry(filename, message):
    root = ET.Element("log")
    entry = ET.SubElement(root, "entry")
    timestamp = ET.SubElement(entry, "timestamp")
    timestamp.text = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_message = ET.SubElement(entry, "message")
    log_message.text = message
    
    tree = ET.ElementTree(root)
    tree.write(filename)

# Create log entries
os.makedirs("Logs", exist_ok=True)
create_log_entry("Logs/update_log.xml", "Log file created. Previous log files were deleted.")
create_log_entry("Logs/error_log.xml", "Error log file created. Previous error log files were deleted.")

# Git commands to add, commit, and push changes to GitHub
os.system("git add .")
os.system('git commit -m "Initialized new XML log files"')
os.system("git push origin main")

# Informing the user about the update completion
print("Update completed! New XML log files have been initialized and pushed to GitHub.")
