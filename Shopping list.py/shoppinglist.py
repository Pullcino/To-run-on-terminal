to_buy = []

question = int(input("welcome to the shopping list choose one option \n1 - add item to list\n2 - Remove item from list\n3 - Display shopping list\n4 - Leave shopping list\n"))

while question != 4:

    if question == 1:

        item = input("Enter the desired item: ")

        to_buy = item.join(to_buy)

        question = int(input("Choose one option \n1 - add item to list\n2 - Remove item from list\n3 - Display shopping list\n4 - Leave shopping list\n"))

    elif question == 2:

        print(f"You have this itens on the list {to_buy}")

        item = input("Enter the desired item you wanna remove: ")

        to_buy.remove(item)

        question = int(input("Choose one option \n1 - add item to list\n2 - Remove item from list\n3 - Display shopping list\n4 - Leave shopping list\n"))

    elif question == 3:

        print(f"That is your shopping list {to_buy}")

        question = int(input("Choose one option \n1 - add item to list\n2 - Remove item from list\n3 - Display shopping list\n4 - Leave shopping list\n"))

    elif question == 4:

        break

print('You leave the shopping list')

