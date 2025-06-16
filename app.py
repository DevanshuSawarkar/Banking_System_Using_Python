import streamlit as st
from Banking.account import SavingsAccount, CurrentAccount
from Banking.transactions import deposit, withdraw

accounts = {}

def create_account():
    acc_type = st.selectbox("Select account type", ["savings", "current"])
    name = st.text_input("Enter account holder's name")
    initial_deposit = st.number_input("Enter initial balance", min_value=0.0)
    
    if st.button("Create Account"):
        if acc_type == 'savings':
            acc = SavingsAccount(name, initial_deposit)
        elif acc_type == 'current':
            acc = CurrentAccount(name, initial_deposit)
        else:
            st.error("Invalid account type.")
            return None
        
        accounts[acc.account_number] = acc
        st.success(f"Account created successfully. Account number: {acc.account_number}")

def login():
    acc_number = st.number_input("Enter your account number", min_value=1000, step=1)
    
    if acc_number in accounts:
        user_acc = accounts[acc_number]
        st.success(f"Welcome {user_acc.name}!")

        while True:
            option = st.selectbox("Choose an option", ["Deposit", "Withdraw", "Check Balance", "Exit"])
            
            if option == 'Deposit':
                amount = st.number_input("Enter amount to deposit", min_value=0.0)
                if st.button("Deposit"):
                    deposit(user_acc, amount)
            elif option == 'Withdraw':
                amount = st.number_input("Enter amount to withdraw", min_value=0.0)
                if st.button("Withdraw"):
                    withdraw(user_acc, amount)
            elif option == 'Check Balance':
                user_acc.display_balance()
            elif option == 'Exit':
                st.success("Exiting...")
                break
    else:
        st.error("Account not found. Please check your account number.")

def main():
    st.title("SIT Banking System")
    option = st.selectbox("Choose an option", ["Create Account", "Login", "Exit"])
    
    if option == 'Create Account':
        create_account()
    elif option == 'Login':
        login()
    elif option == 'Exit':
        st.success("Thank you for using the Banking System. Goodbye!")

main()
