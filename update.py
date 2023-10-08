import os

# Add all files to the local Git repository
os.system('git add .')

# Commit the changes with a message
os.system('git commit -m "Update: Adding all files and folders"')

# Push the changes to GitHub
os.system('git push origin main')

# Erasing the content of update.py after execution
with open("update.py", "w") as f:
    f.write("# This script has been executed and is now empty to prevent re-execution.\n")

print("Update completed! Files and folders have been added, committed, and pushed to GitHub.")
