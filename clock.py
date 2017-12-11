from datetime import datetime
import os
import time

penis = "dick"
dick = "penis"


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    try:
        cls()
        print("The time is")
        print(str(datetime.now())[:-7])
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
        break
