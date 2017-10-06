# Nicer cipher by Email
from cipher_keys import bin_key
from cipher_keys import caesar_key
# Conversion from letters to binary


def binariate(text, key):
    output = ""

    output += "In my encoding, this would make:\n"
    for c in text:
        output += format(key.index(c), '06b') + ' '

    output += "\nIn ASCII coding, that would be: \n"
    for c in text:
        output += format(ord(c), '08b') + ' '

    return output


# Caesar cipher generator


def caesar(steps, text, key):
    stepped = ""

    for char in text:  # For every char in the input
        if char == " ":  # Check if char is whitespace, in that case just add a whitespace
            stepped += char
        elif (key.index(char) + steps) > (len(key) - 1):  # Else if the address we are looking for overflows, go to the beginning and add correct char
            stepped += key[((key.index(char) + steps) - len(key))]
        else:  # Else just add the char that is n steps away
            stepped += key[(key.index(char) + steps)]

    return stepped


ch = input("Select a choice, 1 for binary, 2 for caesar: ")

if ch is "1":
    print(binariate(input("Text to convert: "), bin_key))
elif ch is "2":
    print(caesar(text=input('Text to chiffrera: '), steps=int(input("How many steps? ")), key=caesar_key))
