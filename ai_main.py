
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
            user_input = input("\nYou can type 'stop' to stop AI Main: ")
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
