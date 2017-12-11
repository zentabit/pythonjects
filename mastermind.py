from random import randint as rand


def contains(array, number):
    i = 0
    while i < len(array):
        if array[i] == number:
            return True
        i += 1
    return False


def mastermind():
    comb = [rand(0,9), rand(0,9), rand(0,9), rand(0,9)]
    correct_guesses = 0
    i = 0
    guess = 0
    guessing = ""

    while correct_guesses < len(comb):
        guess = int(input())

        if contains(comb, guess):
            guessing += "x"
            correct_guesses += 1
        else:
            guessing += "o"

        print(guessing)
        i += 1

    print("Correct! It took #{i} guesses.")

    return i

mastermind()
