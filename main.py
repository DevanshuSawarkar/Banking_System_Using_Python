from Banking.account import SavingsAccount, CurrentAccount
from Banking.transactions import deposit, withdraw

accounts = {}

def create_account():
    name = input("Enter your name: ").strip()
    acc_type = input("Enter account type (savings/account): ").strip().lower()
    initial_deposit = float(input("Enter initial deposit amount: "))
    if acc_type == 'savings':
        acc = SavingsAccount(name, initial_deposit)
    elif acc_type == 'current':
        acc = CurrentAccount(name, initial_deposit)
    else:
        print("Invalid account type. Please choose 'savings' or 'current'.")
        return None
    
    accounts[acc.account_number] = acc
    print(f"Account created successfully. Account number: {acc.account_number}")

def login():
    acc_number = int(input("Enter your account number: "))
    if acc_number in accounts:
        user_acc = accounts[acc_number]
        print(f"Welcome {user_acc.name}!")
        while True:
            print("\n1. Deposit")
            print("\n2. Withdraw")
            print("\n3. Check Balance")
            print("\n4. Logout")
            if isinstance(user_acc, SavingsAccount):
                print("\n5. Calculate Interest")
            
            choice = input("Choose an option: ")
            if choice == '1':
                amount = float(input("Enter amount to deposit: "))
                deposit(user_acc, amount)
            elif choice == '2':
                amount = float(input("Enter amount to withdraw: "))
                withdraw(user_acc, amount)
            elif choice == '3':
                print(f"Curernt balance: {user_acc.get_balance()}")
            elif choice == '5' and isinstance(user_acc, SavingsAccount):
                user_acc.calculate_interest()
            elif choice == '4':
                print("Logging out...")
                break
            else:
                print("Invalid choice. Please choose a valid option!")
    else:
        print("Account not found. Please check your account number.")

def main():
    print("\nWelcome to SBI Bank!".center(100,'-'))
    print("Nagpur SIT Branch".center(100,'-'))

    while True:
        print("\n1. Create Account")
        print("\n2. Login")
        print("\n3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            create_account()
        elif choice == '2':
            login()
        elif choice == '3':
            print("Thank you for using SBI Bank. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option!")

if __name__ == "__main__":
    main()