def show_menu():

    print("\nMenu of the contact list")
    print("1 - Add a contact")
    print("2 - change contact")
    print("3 - remove contact")
    print("4 - show contact list")
    print("5 - close program")

def add_contact(contacts):

    name = input("Digit the name of the contact: ")
    number = input("Digit the number of the contact: ")

    contacts[name] = number

    print("\nContact added with sucess")

def change_contact(contacts):

    actual_name = input("Digit the name of the contact you wanna change")

    if actual_name in contacts:

        new_name = input("Digit the new name (press enter without typing to keep the current name): ")
        new_number = input("Digit the new number (press enter without typing to keep the current name): ")

        if new_name :

            if new_name in contacts:

                print("\nThis contact already exist try another name ")

                return
            
            contacts[new_name] = contacts[actual_name]

            del contacts[actual_name]

        else:

            new_name = actual_name

        if new_number:

            contacts[new_name] = new_number

        print("Contact chaged with sucess")

    else:

        print("This contact dont exist")


def remove_contact(contacts):

    question = input("\nWhich contact you want to remove")

    if question in contacts:

        contacts.pop(question)

        print("\nThe contact was successfully removed")

    else:

        print("This contact dont exist")

def show_contacts(contacts):

    for name, number in contacts.items():

        print(f"Name: {name} | Number:{number}")



def main():

    contacts = {}

    while True:

        show_menu()

        option = input("\nChoose one option: ")

        if option == "1":

            add_contact(contacts)

        elif option == "2":

            change_contact(contacts)

        elif option == "3":

            remove_contact(contacts)

        elif option == "4":

            show_contacts(contacts)

        elif option == "5":

            break


main()
print("\nYou close the program")
        

