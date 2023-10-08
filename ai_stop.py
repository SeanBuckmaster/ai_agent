
import os

def create_stop_flag():
    with open("stop_flag.txt", "w") as file:
        file.write("Stop")

if __name__ == "__main__":
    create_stop_flag()
    print("Stop flag created. ai_main.py, ah_turk.py, and ai_update.py will stop on the next loop check.")
