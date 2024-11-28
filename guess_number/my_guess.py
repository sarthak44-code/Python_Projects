import random

def guess(x):
    random_number = random.randint(1, x)
    guess_number = 0
    while guess_number != random_number:
        guess_number = int(input(f"Guess a number between 1 and {x}: "))
        if guess_number < random_number:
            print(f"{guess_number} is less than the random number")
        elif guess_number > random_number:
            print(f"{guess_number} is greater than the random number ")

    print(f"you have guessed the {random_number} correctly! ")

guess(10)

