# update.py

import os
import time

# Updating the ai_main.py with improved stopping mechanism
ai_main_code = """
import threading
import time

def main_loop(stop_event):
    while not stop_event.is_set():
        # Your main loop code here
        print("|", end="", flush=True)
        for _ in range(60):  # Check the stop event every second for a minute
            if stop_event.is_set():
                break
            time.sleep(1)

def management_tasks(stop_event):
    while not stop_event.is_set():
        # Your management tasks code here
        print("/", end="", flush=True)
        for _ in range(30):  # Check the stop event every second for 30 seconds
            if stop_event.is_set():
                break
            time.sleep(1)

def start_ai():
    stop_event = threading.Event()
    main_thread = threading.Thread(target=main_loop, args=(stop_event,))
    management_thread = threading.Thread(target=management_tasks, args=(stop_event,))

    main_thread.start()
    management_thread.start()

    try:
        while True:
            user_input = input("\\nYou can type 'stop' to stop AI Main: ")
            if user_input.lower() == 'stop':
                print("Stopping AI Main...")
                stop_event.set()
                break
    except KeyboardInterrupt:
        print("Stopping AI Main...")
        stop_event.set()

    main_thread.join()
    management_thread.join()

if __name__ == "__main__":
    start_ai()
"""

# Writing the updated code to ai_main.py
with open("ai_main.py", "w") as file:
    file.write(ai_main_code)

# Git commands to add, commit, and push changes to GitHub
os.system("git add .")
os.system('git commit -m "Improved stopping mechanism in ai_main.py"')
os.system("git push origin main")

# Informing the user about the update completion
print("Update completed! The stopping mechanism in ai_main.py has been improved and pushed to GitHub.")
