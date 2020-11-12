import re
import random
class BankAccount:
    def __init__(self, full_name, account_number, routing_number, balance):
        self.name = full_name
        self.account = account_number
        self.routing = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f'Amount Deposited: ${amount}')
        return (f'Account balance: ${self.balance}')
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < amount:
            self.balance = self.balance - 10
            print(f'Insufficient funds. You have been charged an overdraft fee of $10.')
        elif self.balance > amount:
            print(f'Amount Withdrawn: ${amount}')
        return (f'Account balance: ${self.balance}')

    def get_balance(self):
        print(f'Your account balance is: ${self.balance}')
        return self.balance

    def add_interest(self):
        interest = self.balance * 0.00083
        self.balance += interest
        return (f'After your monthly interest: ${self.balance}')
    
    def print_receipt(self):
        print(self.name)
        account = re.sub('\d', '*', str(self.account), 4)
        print(f'Account No.: {account}')
        print(f'Routing No.: {self.routing}')
        print(f'Balance: ${self.balance}')

omar = BankAccount('Omar Lopez', random.randint(10000000,99999999), 123456789, 0)
abel = BankAccount('Abel Pineda', random.randint(10000000,99999999), 123456789, 0)
edgar = BankAccount('Edgar Ulloa', random.randint(10000000,99999999), 123456789, 0)

print(f'Welcome to Terminal ATM!')
print(f'Please enter your first name.')

user = ""

user = input('What is your first name?:')
while True:
    if user == 'omar':
        choice = input(""" Please choose from the following options: 
        1. Deposit money into account
        2. Withdraw money from account
        3. View balance
        4. View monthly interest
        5. Print out receipt
        6. Done
        """)
        if choice == "1":
            amount = int(input('How much money would you like to deposit?'))
            print(omar.deposit(amount))
        elif choice == "2":
            amount = int(input('How much money would you like to withdraw?'))
            print(omar.withdraw(amount))
        elif choice == "3":
            print(omar.get_balance())
        elif choice == "4":
            print(omar.add_interest())
        elif choice == "5":
            print(omar.print_receipt())
        elif choice == "6":
            print(f'Thank you for using Terminal ATM, enjoy your day!')
            break
    elif user == 'abel':
        choice = input(""" Please choose from the following options: 
        1. Deposit money into account
        2. Withdraw money from account
        3. View balance
        4. View monthly interest
        5. Print out receipt
        6. Done
        """)
        if choice == "1":
            amount = int(input('How much money would you like to deposit?'))
            print(abel.deposit(amount))
        elif choice == "2":
            amount = int(input('How much money would you like to withdraw?'))
            print(abel.withdraw(amount))
        elif choice == "3":
            print(abel.get_balance())
        elif choice == "4":
            print(abel.add_interest())
        elif choice == "5":
            print(abel.print_receipt())
        elif choice == "6":
            print(f'Thank you for using Terminal ATM, enjoy your day!')
            break
    elif user == 'edgar':
        choice = input(""" Please choose from the following options: 
        1. Deposit money into account
        2. Withdraw money from account
        3. View balance
        4. View monthly interest
        5. Print out receipt
        6. Done
        """)
        if choice == "1":
            amount = int(input('How much money would you like to deposit?'))
            print(edgar.deposit(amount))
        elif choice == "2":
            amount = int(input('How much money would you like to withdraw?'))
            print(edgar.withdraw(amount))
        elif choice == "3":
            print(edgar.get_balance())
        elif choice == "4":
            print(edgar.add_interest())
        elif choice == "5":
            print(edgar.print_receipt())
        elif choice == "6":
            print(f'Thank you for using Terminal ATM, enjoy your day!')
            break