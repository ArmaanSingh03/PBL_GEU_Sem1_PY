class Expense:
    def __init__(self, amount, description):
        self.amount = amount
        self.description = description

    def __str__(self):
        return f"{self.description}: {self.amount:.2f}"

    def calculate_amount(self):
        return self.amount

class FixedExpense(Expense):
    def __init__(self, amount, description):
        super().__init__(amount, description)

    FixExp = ()

    def calculate_amount(self):
        return self.amount


class VariableExpense(Expense):
    def __init__(self, amount, description):
        super().__init__(amount, description)

    VarExp = {}

    def calculate_amount(self):
        return self.amount

expenses = {}
fixed_info = ()
categories = set()
expense_id = 1

while True:
    print("\n--- Expense Management ---")
    print("1. Add Fixed Expense")
    print("2. Add Variable Expense")
    print("3. Display Expenses")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1" or choice == "2":
        description = input("Enter description: ")
        amount = float(input("Enter amount: "))

        if choice == "1":
            expense = FixedExpense(amount, description)
            fixed_info += ((description, amount),)
            categories.add("Fixed")
        else:
            expense = VariableExpense(amount, description)
            categories.add("Variable")

        expenses[expense_id] = expense
        expense_id += 1
        print("Expense added successfully!")

    elif choice == "3":
        for key, expense in expenses.items():
            print(key, expense)

        print("Fixed Expenses:", fixed_info)
        print("Categories:", categories)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")



