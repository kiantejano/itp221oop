class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def give_raise(self, amount):
        if amount > 0:
            self.salary += amount
            print(f"Salary increased by PHP{amount}. New salary: PHP{self.salary}")
        else:
            print("Invalid raise amount.")

    def display_employee(self):
        print(f"Name: {self.name}, Position: {self.position}, Salary: PHP{self.salary}")


employee1 = Employee("Kian Tejano", "Bantay Computeran", 10000)

employee1.display_employee()

while True:
    try:
        amount = float(input("Enter the amount to raise the salary: "))
        if amount > 0:
            employee1.give_raise(amount)
            break
        else:
            print("Invalid raise amount. Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

employee1.display_employee()