# update.py

import os
import shutil

# Rename log files to .xml if they exist
if os.path.exists("Logs/update_log.txt"):
    os.rename("Logs/update_log.txt", "Logs/update_log.xml")

if os.path.exists("Logs/error_log.txt"):
    os.rename("Logs/error_log.txt", "Logs/error_log.xml")

# Git commands to add, commit, and push changes to GitHub
os.system("git add .")
os.system('git commit -m "Changed log files to XML format"')
os.system("git push origin main")

# Informing the user about the update completion
print("Update completed! Log files have been changed to XML format and pushed to GitHub.")

