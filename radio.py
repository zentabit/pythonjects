from random import randint
from random import randrange
import winsound
import time

while True:
	winsound.Beep(randrange(300, 2000), randint(100, 500))
	time.sleep((randrange(0, 500)/1000))

