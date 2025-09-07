option = int(input('Welcome to ATM choose one option\n1 - See my balance\n2 - Deposit\n3 - Withdraw\n4 - Leave '))

balance = 250

def deposit(a, b):

    return (a + b)

def withdraw(a, b):

    return (a - b)

while option != 4:

    if option == 1:

        print(f'This is your balance: {balance}')

        option = int(input('Choose one option\n1 - See my balance\n2 - Deposit\n3 - Withdraw\n4 - Leave '))

    elif option == 2:

        deposit_ask = int(input('How much you wanna deposit: '))

        balance = deposit(deposit_ask, balance)

        print(f'Now this is your balance: {balance}')

        option = int(input('Choose one option\n1 - See my balance\n2 - Deposit\n3 - Withdraw\n4 - Leave '))

    elif option == 3:

        withdraw_ask = int(input('How much you wanna withdraw: '))

        balance = withdraw(balance, withdraw_ask)

        print(f'Now this is your balance: {balance}')

        option = int(input('Choose one option\n1 - See my balance\n2 - Deposit\n3 - Withdraw\n4 - Leave '))

    elif option == 4:

        break

print('You leave the ATM')