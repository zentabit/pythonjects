# define frequencies for the notes
keys = {"C": 293,
        "C4": 293,
        "C5": 523,
        "D": 294,
        "E": 330,
        "F": 349,
        "G": 392,
        "A": 440,
        "B": 494,
        "C#": 277,
        "D#": 311,
        "F#": 370,
        "G#": 415,
        "A#": 466,
        }
# loop for repeated input
while True:
    # input the notes, uppercase them and make it a list
    notes = ((input("Notes plz: ")).upper()).split()
    # empty list for the output to be
    freqs = []

    # try to loop through the list and append the correct frequencies
    try:
        for n in notes:
            freqs.append(keys[n])
    # if note can't be found
    except KeyError:
        print("Oops, looks like you didn't input a valid key, wanna go again?")

    # print the result
    print(freqs)

    # ask if the while-loop should continue, if no, then exit
    if (input("Go again? y/n ")).lower() == "n":
        break
