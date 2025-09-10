to_buy = []

question = int(input("welcome to the shopping list choose one option \n1 - add item to list\n2 - Remove item from list\n3 - Display shopping list\n4 - Leave shopping list\n"))

while question != 4:

    if question == 1:

        item = input("Enter the desired item: ")

        to_buy.append(item)

        question = int(input("Choose one option \n1 - add item to list\n2 - Remove item from list\n3 - Display shopping list\n4 - Leave shopping list\n"))

    elif question == 2:

        if len(to_buy) == 0:

            print("The list is empty")

        else:

            item = input("type the item you want to remove")

            if item in to_buy:

                to_buy.remove(item)

                print(f"You remove the item ")

            else:

                print("That item is not on the list")

        question = int(input("Choose one option \n1 - add item to list\n2 - Remove item from list\n3 - Display shopping list\n4 - Leave shopping list\n"))

    elif question == 3:

        for item in to_buy:

            print("- ", item)

        question = int(input("Choose one option \n1 - add item to list\n2 - Remove item from list\n3 - Display shopping list\n4 - Leave shopping list\n"))

    elif question == 4:

        break

print('You leave the shopping list')

