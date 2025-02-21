class BankAccount:
    def __init__(self, account_number, owner, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. New balance: PHP{self.balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew PHP{amount}. New balance: PHP{self.balance}")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            print("Invalid withdrawal amount.")

    def display_balance(self):
        print(f"Account {self.account_number} - {self.owner} Balance: PHP{self.balance}")


account1 = BankAccount("69420", "Kian Tejano", 10000)

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Display Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        try:
            amount = float(input("Enter amount to deposit: "))
            account1.deposit(amount)
        except ValueError:
            print("Invalid input.")
    elif choice == '2':
        try:
            amount = float(input("Enter amount to withdraw: "))
            account1.withdraw(amount)
        except ValueError:
            print("Invalid input.")
    elif choice == '3':
        account1.display_balance()
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")