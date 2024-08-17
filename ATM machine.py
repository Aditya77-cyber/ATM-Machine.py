class ATM:
    def __init__(self, balance=0):
        self.balance = balance
        self.pin = "1234"  # Default PIN
        self.transaction_history = []

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")
        self.transaction_history.append(f"Balance inquiry: ${self.balance}")

    def withdraw_cash(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")
            self.transaction_history.append(f"Withdrawn: ${amount}")

    def deposit_cash(self, amount):
        self.balance += amount
        print(f"${amount} deposited successfully.")
        self.transaction_history.append(f"Deposited: ${amount}")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.pin:
            self.pin = new_pin
            print("PIN changed successfully.")
            self.transaction_history.append("PIN changed")
        else:
            print("Incorrect old PIN.")

    def print_transaction_history(self):
        if not self.transaction_history:
            print("No transactions yet.")
        else:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)

# Main Function to simulate ATM operations
def atm_simulation():
    atm = ATM(balance=1000)  # Starting with a balance of $1000

    while True:
        print("\nWelcome to the ATM Machine")
        print("1. Check Balance")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            atm.withdraw_cash(amount)
        elif choice == "3":
            amount = float(input("Enter amount to deposit: "))
            atm.deposit_cash(amount)
        elif choice == "4":
            old_pin = input("Enter old PIN: ")
            new_pin = input("Enter new PIN: ")
            atm.change_pin(old_pin, new_pin)
        elif choice == "5":
            atm.print_transaction_history()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the ATM simulation
if __name__ == "__main__":
    atm_simulation()


