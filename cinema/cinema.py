cinema = []

for line in range(4):

    seat = []

    for column in range(10):

        seat.append("A")

    cinema.append(seat)


while True:

    print("Cinema")
    print("1 - View the seats")
    print("2 - Choose one seat")
    print("3 - Leave the cinema")

    choose = int(input("Choose one between the options: (1 - 3)"))

    if choose == 1:

        for line in cinema:

            for seat in line:

                print(seat, end=" ")

            print()

    elif choose == 2:

        line = int(input("Digit the number of the line of your seat (0 - 4)")) 
        seat = int(input("Digit the number of your seat (0 - 9)"))

        cinema[line][seat] = "B"

        for line in cinema:

            for seat in line:

                print(seat, end=" ")

            print()

    elif choose == 3:

        break

print("You leave the program")