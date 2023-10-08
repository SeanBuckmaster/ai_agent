
import time
import threading

def main_loop(task_processor_func):
    try:
        print("|/", end="", flush=True)
        while True:
            # Your main loop code here
            # ...
            # Call the task processor function
            task_processor_func()
            time.sleep(1)
            print("\r|", end="", flush=True)
            time.sleep(1)
            print("\r/", end="", flush=True)
    except KeyboardInterrupt:
        print("\nStopping AI Main...")
