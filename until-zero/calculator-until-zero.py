number = int(input("Digit a number: "))

print("Now we gonna subtract until this number turn to zero")

def sub(a, b):

    return a - b

while number > 0:

    new_number = int(input("Enter the number you want to subtract."))

    print(sub(number, new_number))

    number
