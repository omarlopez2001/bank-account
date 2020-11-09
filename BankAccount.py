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