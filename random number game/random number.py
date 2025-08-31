import random

number = random.randint(1, 10)

trys = 3

while trys != 0:

    guess = int(input(f'Try to guess the number between 1 and 10\nyou have {trys} attemps: '))

    if guess != number:

        trys = trys - 1

    elif guess == number:

        print('You win')

        break

    if trys == 0:

        print('You lose')

print('Game over')
        


