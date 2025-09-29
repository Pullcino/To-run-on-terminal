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

def main():

    contacts = {}

    while True:

        show_menu()

        option = input("Choose one option: ")

        if option == "1":

            add_contact(contacts)

        

