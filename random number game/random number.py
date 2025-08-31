import random

number = random.randint(1, 10)

trys = 3

while trys > 0 or guess != number :

    guess = int(input(f'Try to guess the number between 1 and 10\nyou have {trys} attemps: '))
    
    if guess != number:

        trys = trys - 1

        guess = int(input(f'Try to guess the number between 1 and 10\nyou have {sub} attemps: '))

    else:

        print(f'Good job youre right the number is {number}')
