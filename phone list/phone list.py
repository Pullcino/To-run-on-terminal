def show_menu():

    print("Menu of the contact list")
    print("1 - Add a contact")
    print("2 - change contact")
    print("3 - remove contact")
    print("4 - show contact list")
    print("5 - close program")

def add_contact(contacts):

    name = input("Digit the name of the contact: ")
    number = input("Digit the number of the contact: ")

    contacts[name] = number

    print("Contact added with sucess")

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

    question = input("Which contact")



def main():

    contacts = {}

    while True:

        show_menu()

        option = input("Choose one option: ")

        if option == "1":

            add_contact(contacts)

        elif option == "2":

            change_contact(contacts)

main()

        

