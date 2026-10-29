import os

EXPENSE_FILE = "expenseFile.txt"
BUDGET_FILE = "budgetFile.txt"

expenses = []
budget = 0


def load_data():
    global budget

    try:
        with open(EXPENSE_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 2:
                    expenses.append(
                        (parts[0], float(parts[1]))
                    )

    except FileNotFoundError:
        print("Expense file not found. Starting fresh.")
    except ValueError:
        print("Invalid expense data found.")

    try:
        with open(BUDGET_FILE, "r") as file:
            budget = float(file.read())

    except FileNotFoundError:
        print("Budget file not found. Starting with 0.")
    except ValueError:
        print("Invalid budget data. Using 0.")
        budget = 0


def save_data():
    with open(EXPENSE_FILE, "w") as file:
        for name, amount in expenses:
            file.write(f"{name},{amount}\n")

    with open(BUDGET_FILE, "w") as file:
        file.write(str(budget))


def add_expense():
    try:
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be positive.")
            return

        expenses.append((name, amount))
        save_data()
        print("Expense saved successfully.")

    except ValueError:
        print("Please enter a valid amount.")


def set_budget():
    global budget

    try:
        budget = float(input("Enter total budget: "))

        if budget < 0:
            print("Budget cannot be negative.")
            return

        save_data()
        print("Budget saved successfully.")

    except ValueError:
        print("Please enter a valid budget.")


def view_records():
    print("\nBudget:", budget)
    print("Expenses:")

    for name, amount in expenses:
        print(name, "-", amount)

    total = sum(amount for name, amount in expenses)
    print("Total Expenses:", total)
    print("Remaining Budget:", budget - total)


load_data()

while True:
    print("\n1. Add Expense")
    print("2. Set Budget")
    print("3. View Records")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        set_budget()
    elif choice == "3":
        view_records()
    elif choice == "4":
        save_data()
        print("Data saved. Exiting program.")
        break
    else:
        print("Invalid choice.")
