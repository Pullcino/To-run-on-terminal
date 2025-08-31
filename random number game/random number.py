import random

number = random.randint(1, 10)

trys = 3

guess = int(input(f'Try to guess the number between 1 and 10\nyou have {trys} attemps: '))

while trys > 0:
    
    if guess != number:

        trys = trys - 1

        guess = int(input(f'Try to guess the number between 1 and 10\nyou have {trys} attemps: '))

    elif guess == number:

        print('You win')
    
    elif trys == 0:

        print('you lose')
        break


