import random

def computer_guess(x):
    low = 1
    high = x
    feedback = ''

    while feedback != 'c' and low != high:
        guess = random.randint(low, high)
        feedback = input(f'is {guess} too high(h), too low(l) or correct(c)??').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'the number - {guess} is correct!!')

computer_guess(500)