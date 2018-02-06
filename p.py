import math, random, sys
from tqdm import tqdm

print("P-Pi: Calculate pi by probability!\nPlease don't input more than: " + str(sys.maxsize))

while True:
    sump = 0
    x = 0
    p = 0
    one = []
    two = []

    maxval = input("Max value: ")
    maxval = int(maxval)

    print("Generating randints...")

    try:
        for i in tqdm(range(0, maxval)):
            one.append(random.randint(0, maxval))
            two.append(random.randint(0, maxval))
    except MemoryError:
        print ("För mycket saker händer just nu!")
        input("Enter to exit...")
        break

    print("Calculating gcds...")

    for val in tqdm(range(0, len(one))):
        gcd = math.gcd(one[val], two[val])
        if gcd == 1:
            sump += 1

    print("Calculating pi...")
    p = sump / maxval
    x = math.sqrt(6 / p)
    print("This pie was: " + str(x) + "\n")

    if input("Go again? y/n:") == "n":
        break
