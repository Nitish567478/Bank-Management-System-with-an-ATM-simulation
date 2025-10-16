import json
import os

DATA_FILE = "accounts.json"

if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump({}, f)

def load_accounts():
    with open(DATA_FILE, "r") as f:
        return json.load(f)

def save_accounts(accounts):
    with open(DATA_FILE, "w") as f:
        json.dump(accounts, f, indent=4)

def verify_pin(accounts, account_no):
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")
        if account_no in accounts and accounts[account_no]["pin"] == entered_pin:
            return True
        else:
            attempts -= 1
            print(f"Invalid PIN! Attempts left: {attempts}")
    print("Your card has been blocked due to 3 incorrect attempts.")
    return False

def user_menu(accounts, account_no):
    while True:
        print("\n--- Welcome,", accounts[account_no]["name"], "---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Your current balance: ₹", accounts[account_no]["balance"])

        elif choice == "2":
            amount = float(input("Enter amount to deposit: "))
            if amount > 0:
                accounts[account_no]["balance"] += amount
                accounts[account_no]["transactions"].append(f"Deposited ₹{amount}")
                print(f"₹{amount} deposited successfully.")
            else:
                print("Invalid amount.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: "))
            if 0 < amount <= accounts[account_no]["balance"]:
                accounts[account_no]["balance"] -= amount
                accounts[account_no]["transactions"].append(f"Withdrew ₹{amount}")
                print(f"₹{amount} withdrawn successfully.")
            else:
                print("Insufficient balance or invalid amount.")

        elif choice == "4":
            new_pin = input("Enter your new 4-digit PIN: ")
            accounts[account_no]["pin"] = new_pin
            print("PIN changed successfully.")

        elif choice == "5":
            print("\n--- Transaction History ---")
            if accounts[account_no]["transactions"]:
                for t in accounts[account_no]["transactions"]:
                    print(t)
            else:
                print("No transactions yet.")

        elif choice == "6":
            print("Thank you for using Apna Bank ATM!")
            break

        else:
            print("Invalid choice. Try again.")

        save_accounts(accounts)

        cont = input("\nDo you want to continue? Press 1 to continue or any other key to exit: ")
        if cont != "1":
            print("Thank you for using Apna Bank ATM!")
            break


def main():
    accounts = load_accounts()

    print("\nWelcome to Apna Bank ATM System")
    print("1. Existing User")
    print("2. New User Registration")
    choice = input("Enter your choice: ")

    if choice == "1":
        account_no = input("Enter your account number: ")
        if verify_pin(accounts, account_no):
            user_menu(accounts, account_no)

    elif choice == "2":
        account_no = input("Create account number: ")
        if account_no in accounts:
            print("Account already exists!")
            return
        name = input("Enter your name: ")
        pin = input("Set your 4-digit PIN: ")  
        accounts[account_no] = {
            "name": name,
            "pin": pin,
            "balance": 0,
            "transactions": []
        }
        save_accounts(accounts)
        print("Account created successfully! Please login again to access your account.")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
