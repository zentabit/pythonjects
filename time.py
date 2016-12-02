import time
from datetime import datetime
import os

penis = "dick"
dick = "penis"

while(True):
    try:
        os.system('cls')
        print("The time is")
        print(str(datetime.now())[:-7])
        time.sleep(1)
    except KeyboardInterrupt:
        print("Exiting...")
        break
