def sum(a, b):
    return (a + b)

def sub(a, b):
    return (a - b)

def div(a, b):
    return (a / b)

def mult(a, b):
    return (a * b)

calculator = int(input('Welcome to the program choose one between the next options: \n1 - Sum \n2 - Subtraction \n3 - Division \n4 - Multiplication \n5 - leave the program \nOption: '))

while calculator != 5:

    if calculator == 1 :

        number1 = int(input('Digit the first number: '))
        number2 = int(input('Digit the last number: '))

        result = sum(number1, number2)

        print(f'The result of the sum is {result}')

        calculator = int(input('choose one between the next options: \n1 - Sum \n2 - Subtraction \n3 - Division \n4 - Multiplication \n5 - leave the program \nOption: '))

    elif calculator == 2 :

        number1 = int(input('Digit the first number: '))
        number2 = int(input('Digit the last number: '))

        result = sub(number1, number2)

        print(f'The result of the subtraction is: {result}')

        calculator = int(input('choose one between the next options: \n1 - Sum \n2 - Subtraction \n3 - Division \n4 - Multiplication \n5 - leave the program \nOption: '))

    elif calculator == 3 :

        number1 = int(input('Digit the first number: '))
        number2 = int(input('Digit the last number: '))

        result = div(number1, number2)
        print(f'The result of the division is: {result}')

        calculator = int(input('choose one between the next options: \n1 - Sum \n2 - Subtraction \n3 - Division \n4 - Multiplication \n5 - leave the program \nOption: '))

    elif calculator == 4:

        number1 = int(input('Digit the first number: '))
        number2 = int(input('Digit the last number: '))

        result = mult(number1, number2)
        print(f'The result of the multiplication is: {result}')

        calculator = int(input('choose one between the next options: \n1 - Sum \n2 - Subtraction \n3 - Division \n4 - Multiplication \n5 - leave the program \nOption: '))

    elif calculator > 5:

        print('That option dont exist')
        calculator = int(input('choose one between the next options: \n1 - Sum \n2 - Subtraction \n3 - Division \n4 - Multiplication \n5 - leave the program \nOption: '))

print('You leave the program')