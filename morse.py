import winsound
from time import sleep


alphabet = {
    'a': ['s', 'l'],
    'b': ['l', 's', 's', 's'],
    'c': ['l', 's', 'l', 's'],
    'd': ['l', 's', 's'],
    'e': ['s'],
    'f': ['s', 's', 'l', 's'],
    'g': ['l','l','s'],
    'h': ['s','s','s','s'],
    'i': ['s','s'],
    'j': ['s','l','l','l'],
    'k': ['l','s','l'],
    'l': ['s','l','s','s'],
    'm': ['l', 'l'],
    'n': ['l', 's'],
    'o': ['l', 'l', 'l'],
    'p': ['s','l', 'l','s'],
    'q': ['l','l','s','l'],
    'r': ['s','l', 's'],
    's': ['s', 's', 's'],
    't': ['l'],
    'u': ['s','s','l'],
    'v': ['s','s','s','l'],
    'w': ['s','l','l'],
    'x': ['l','s','s','l'],
    'y': ['l', 's','l','l'],
    'z': ['l','l','s','s']
}

def make_sound(letter):
    for beep in alphabet[letter]:
        if beep == 'l':
            print('-', end=' ')
            winsound.Beep(400, 500)
            sleep(0.3)
        else:
            print('*',  end=' ')
            winsound.Beep(400, 250)
            sleep(0.3)

def speak_morse(word):
    for letter in word:
        if letter == ' ':
            print(' ',  end=' ')
            sleep(1)
        else:
            make_sound(letter)
            sleep(0.5)

speak_morse('sos sos')
