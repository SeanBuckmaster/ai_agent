import os

# Update the ai_main.py
ai_main_code = """
import threading
import time

def main_loop():
    while not stop_event.is_set():
        # Your main loop logic here
        time.sleep(2)  # Using ChatGPT 3.5 every 2 seconds

def check_stop():
    while True:
        user_input = input("\\nYou can type 'stop' to stop AI Main: ")
        if user_input.strip().lower() == 'stop':
            print("Stopping AI Main...")
            stop_event.set()
            break

def management_tasks():
    while not stop_event.is_set():
        # Your management and verification logic here
        time.sleep(60)  # Using ChatGPT 4.0 every 60 seconds

stop_event = threading.Event()

main_thread = threading.Thread(target=main_loop)
stop_thread = threading.Thread(target=check_stop)
management_thread = threading.Thread(target=management_tasks)

print("AI Main is running. Monitoring tasks and awaiting user input...")

main_thread.start()
stop_thread.start()
management_thread.start()

main_thread.join()
stop_thread.join()
management_thread.join()
"""

with open("ai_main.py", "w") as file:
    file.write(ai_main_code)

# Git commands to add, commit, and push changes to GitHub
os.system("git add .")
os.system('git commit -m "Updated ai_main.py with non-intrusive running message"')
os.system("git push origin main")

# Informing the user about the update completion
print("Update completed! ai_main.py has been updated and changes have been pushed to GitHub.")
