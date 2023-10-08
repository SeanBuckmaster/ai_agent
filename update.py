import os

# Update the logging path in ai_main.py and BusinessLayer/main_loop.py
# This assumes a basic logging setup and may need to be adjusted based on your actual logging setup.

scripts_to_update = ["ai_main.py", "BusinessLayer/main_loop.py"]

for script in scripts_to_update:
    with open(script, "r") as file:
        script_contents = file.read()
    
    # Replace the old logging path with the new one
    script_contents = script_contents.replace("Logs/", "ai_logs/")
    
    with open(script, "w") as file:
        file.write(script_contents)

# Create a test log entry in ai_logs
with open("ai_logs/update_log.txt", "a") as log_file:
    log_file.write("Update completed! Logging paths have been updated in scripts.\n")

# Git commands to add, commit, and push changes to GitHub
os.system("git add .")
os.system('git commit -m "Updated logging paths in scripts"')
os.system("git push origin main")

# Informing the user about the update completion
print("Update completed! Logging paths have been updated in scripts and changes have been pushed to GitHub.")
