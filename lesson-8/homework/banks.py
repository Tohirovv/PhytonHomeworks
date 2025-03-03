class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return self.name + " " + str(self.balance)


class Bank:
    def __init__(self):
        self.accounts = dict()
        self.file_name = "accounts.txt"
        self.number = 1
        for line in self.load_from_file:
            account_number, name, balance = line.strip().split(", ")
            account_number = int(account_number)
            balance = float(balance)
            self.accounts[account_number] = Account(account_number, name, balance)
        if self.accounts:
            self.number = max(self.accounts) + 1

    def create_account(self, name, initial_deposit):
        if not isinstance(name, str):
            raise ValueError("Name should be a string!")
        if not isinstance(initial_deposit, (int, float)):
            raise ValueError("Deposit should be a number!")

        acc_number = self.number
        self.number += 1
        self.accounts[acc_number] = Account(acc_number, name, initial_deposit)
        self.save_to_file(self.accounts[acc_number])

    def view_account(self, account_number):
        if not isinstance(account_number, int):
            raise ValueError("Account number should be an integer!")
        if account_number not in self.accounts:
            raise ValueError("Account number not found!")
        return self.accounts[account_number]

    def deposit(self, account_number, amount):
        if not isinstance(account_number, int):
            raise ValueError("Account number should be an integer!")
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount should be a number!")
        self.accounts[account_number].balance += amount
        self.save_to_file(self.accounts[account_number])

    def withdraw(self, account_number, amount):
        if not isinstance(account_number, int):
            raise ValueError("Account number should be an integer!")
        if not isinstance(amount, (int, float)):
            raise ValueError("Amount should be a number!")
        if amount > self.accounts[account_number].balance:
            raise ValueError("Amount should be less than or equal to account balance!")
        self.accounts[account_number].balance -= amount
        self.save_to_file(self.accounts[account_number])

    def save_to_file(self, acc):
        accounts = self.load_from_file
        with open(self.file_name, "w") as file:
            found = False
            for line in accounts:
                account = line.strip().split(", ")
                if account[0] == str(acc.account_number):
                    found = True
                    account[1] = acc.name
                    account[2] = str(acc.balance)
                    file.write(", ".join(account) + "\n")
                else:
                    file.write(line)
            if not found:
                file.write(f"{acc.account_number}, {acc.name}, {acc.balance}\n")

    @property
    def load_from_file(self):
        try:
            with open(self.file_name, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            with open(self.file_name, "w"):
                lines = []
        return lines


bank1 = Bank()
bank1.create_account("MR", 1200)
print(bank1.view_account(1))
bank1.deposit(2, 300)