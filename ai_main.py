
import threading
import time
import sys

def spinning_cursor():
    while not stop_event.is_set():
        for cursor in '\|/-':
            sys.stdout.write(cursor)
            sys.stdout.flush()
            time.sleep(0.1)
            sys.stdout.write('\r')

def main_loop():
    while not stop_event.is_set():
        # Your main loop logic here
        time.sleep(2)  # Using ChatGPT 3.5 every 2 seconds

def check_stop():
    while True:
        user_input = input("\nYou can type 'stop' to stop AI Main: ")
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
cursor_thread = threading.Thread(target=spinning_cursor)

main_thread.start()
stop_thread.start()
management_thread.start()
cursor_thread.start()

main_thread.join()
stop_thread.join()
management_thread.join()
cursor_thread.join()
