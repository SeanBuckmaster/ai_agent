import os
import shutil

# Delete the old Logs directory if it exists
if os.path.exists("Logs"):
    shutil.rmtree("Logs")

# Create a new ai_logs directory
os.makedirs("ai_logs", exist_ok=True)

# Git commands to add, commit, and push changes to GitHub
os.system("git add .")
os.system('git commit -m "Replaced Logs directory with ai_logs"')
os.system("git push origin main")

# Informing the user about the update completion
print("Update completed! Logs directory has been replaced with ai_logs and changes have been pushed to GitHub.")
