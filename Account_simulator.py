# 💰 Bank Account Simulator
# Author: Divya Reddy

class BankAccount:
    """A simple class representing a bank account."""

    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"✅ Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("❌ Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"💸 Withdrew ₹{amount}. Remaining balance: ₹{self.balance}")
        else:
            print("⚠️ Insufficient funds or invalid amount!")

    def display_balance(self):
        print(f"👤 Account Holder: {self.account_holder}")
        print(f"💰 Current Balance: ₹{self.balance}\n")


# Inheritance Example
class SavingsAccount(BankAccount):
    """A subclass that adds interest to the account."""

    def __init__(self, account_holder, balance=0, interest_rate=0.05):
        super().__init__(account_holder, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"💹 Interest of ₹{interest:.2f} added. New balance: ₹{self.balance:.2f}\n")


# Main function
def main():
    print("=== 🏦 Welcome to Divya's Bank ===\n")
    name = input("Enter account holder name: ")
    account = SavingsAccount(name, balance=5000)

    while True:
        print("\n1️⃣ Deposit Money")
        print("2️⃣ Withdraw Money")
        print("3️⃣ Check Balance")
        print("4️⃣ Apply Interest")
        print("5️⃣ Exit")
        choice = input("\nChoose an option: ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: ₹"))
            account.deposit(amount)
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: ₹"))
            account.withdraw(amount)
        elif choice == "3":
            account.display_balance()
        elif choice == "4":
            account.apply_interest()
        elif choice == "5":
            print("👋 Thank you for using Divya's Bank. Have a great day!")
            break
        else:
            print("❌ Invalid option! Please try again.\n")


if __name__ == "__main__":
    main()
