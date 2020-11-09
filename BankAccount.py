class BankAccount:
    balance = 0
    def __init__(self, full_name, account_number, routing_number, balance):
        self.name = full_name
        self.account = account_number
        self.routing = routing_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount + self.balance
        print(f'Amount Deposited: {amount}')
        return self.balance
    
    def withdraw(self, amount):
        self.balance = self.balance - amount
        if self.balance < amount:
            self.balance = self.balance - 10
            print(f'Insufficient funds. You have been charged an overdraft fee of $10.')
        elif self.balance > amount:
            print(f'Amount Withdrawn: {amount}')
        return self.balance

    def get_balance(self):
        print(f'Your account balance is: {self.balance}')
        return self.balance