import sys
def own():
    print ("Google owns you",)
    
print ("Welcome to the google owner!")
inp = input ("How many times do you want Google to own you? ")
try:
    x = int(inp)
except ValueError:
    print("Ahah no.")
    sys.exit()

if x > 1000:
    print ("Well, that's too much")
elif x <= 1000:
    for n in range(x):
        own()
else:
    print ("Sorry, didn't catch that!")

input("Press enter...")
