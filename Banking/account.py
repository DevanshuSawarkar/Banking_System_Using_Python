class BankAccount:

    account_counter = 1000

    def __init__(self, name, balance=0):
        self.account_number = BankAccount.account_counter
        BankAccount.account_counter += 1
        self.name = name
        self.__balance = balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposit of ₹{amount} successful. New balance: ₹{self.__balance}")
            return True
        else:
            print("Depodit amount must be positive")
            return False
    
    def withdraw(self, amount):
        if amount > 0:
            if self.__balance >= amount:
                self.__balance -= amount
                print(f"Withdrawal of ₹{amount} successful. New balance: ₹{self.__balance}")
                return True
            else:
                print("Insufficient balance")
                return False
        else:
            return False
    
    def display_balance(self):
        print(f"Account Number: {self.account_number}, Account Holder: {self.name}, Balance: ₹{self.__balance}")

class SavingsAccount(BankAccount):
    def __init__(self, name, balance=0, interest_rate=0.05):
        super().__init__(name, balance)
        self.interest_rate = interest_rate
    
    def calculate_interest(self):
        months = int(input("How many months to calculate interest: "))
        interest = self.get_balance() * self.interest_rate * months
        self.deposit(interest)
        print(f"Interest applied: ₹{interest}. New balance: ₹{self.get_balance()}")

class CurrentAccount(BankAccount):
    def __init__(self, name, balance=0, overdraft_limit=100000):
        super().init(name, balance)
        self.overdraft_limit = overdraft_limit