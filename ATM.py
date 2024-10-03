class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return f"Deposited ${amount} successfully."
        else:
            return "Invalid amount for deposit."

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return f"Withdrew ${amount} successfully."
        else:
            return "Invalid amount for withdrawal."

    def transfer(self, recipient, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient.account_holder}")
            return f"Transferred ${amount} to {recipient.account_holder} successfully."
        else:
            return "Invalid amount for transfer."

    def display_balance(self):
        return f"{self.account_holder}'s balance: ${self.balance}"

    def display_transaction_history(self):
        return "\n".join(self.transaction_history) if self.transaction_history else "No transactions yet."


def main():
    account1 = BankAccount("Alice", 1000)
    account2 = BankAccount("Bob", 500)
    
    while True:
        print("\n*** ATM Menu ***")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Transfer")
        print("4. View Balance")
        print("5. Transaction History")
        print("6. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            amount = float(input("Enter the deposit amount: "))
            print(account1.deposit(amount))
        elif choice == "2":
            amount = float(input("Enter the withdrawal amount: "))
            print(account1.withdraw(amount))
        elif choice == "3":
            amount = float(input("Enter the transfer amount: "))
            print(account1.transfer(account2, amount))
        elif choice == "4":
            print(account1.display_balance())
        elif choice == "5":
            print(account1.display_transaction_history())
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
