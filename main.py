from bank import BankAccount
from bank import Account


def main():
    current_account: BankAccount | None = None

    while True:
        menu = 'Choose operation below:\n'

        x = 1
        if current_account is None:
            menu += f'{x}. Register\n' \
                    f'{x + 1}. Log in\n'
            x += 2

        else:
            menu += f'{x}. Deposit money\n' \
                    f'{x + 1}. Withdraw money\n' \
                    f'{x + 2}. Show money in the account\n' \
                    f'{x + 3}. Convert currency\n' \
                    f'{x + 4}. Logout\n'

        menu += '0. Exit\n'

        command = input(menu)

        if command == '0':
            break
        elif command == '1' and current_account is None:
            name, surname = input('Enter name and surname: \n').split()
            current_account = BankAccount(name, surname)
        elif command == '2' and current_account is None:
            name, surname = input('Enter name and surname: \n').split()
            current_account = BankAccount.get_account(name, surname)

            if current_account is None:
                print('No such account')
            else:
                print('Successfully logged in')
        elif command == '1' and current_account:
            amount = int(input('Enter amount\n'))
            current_account.add(amount)
        elif command == '2' and current_account:
            amount = int(input('Enter amount\n'))
            if not current_account.withdraw(amount):
                print('Not enough money')
        elif command == '3' and current_account:
            print(f'{current_account.wallet} {current_account.account.name}')
        elif command == '4' and current_account:
            currency = input(f'Choose currency from: {", ".join([i.name for i in Account])}\n')

            if currency in [i.name for i in Account]:
                current_account.convert(Account[currency])
            else:
                print('Such currency does not exist')
        elif command == '5' and current_account:
            current_account = None
            print('bye!')


if __name__ == '__main__':
    main()
