import os
from collections import defaultdict
from datetime import datetime
from Display import plot_all_charts

EXPENSE_FILE = "expenseFile.txt"
BUDGET_FILE = "budgetFile.txt"

CATEGORY_BUDGETS = {"Food": 1000, "Transport": 400, "Rent": 5000, "Entertainment": 500}

expenses = []
budget = 0

def show_charts():
    category_totals = defaultdict(float)
    monthly_totals = defaultdict(float)

    for name, category, date, amount in expenses:
        clean_category = category.strip().title()  # "food " and "FOOD" become "Food"
        category_totals[clean_category] += amount
        month = datetime.strptime(date, "%Y-%m-%d").strftime("%Y-%m")
        monthly_totals[month] += amount

    if not expenses:
        print("No expenses to chart yet.")
        return

    budgets = {k.strip().title(): v for k, v in CATEGORY_BUDGETS.items()}

    plot_all_charts(dict(category_totals), dict(sorted(monthly_totals.items())), budgets)

def load_data():
    global budget

    try:
        with open(EXPENSE_FILE, "r") as file:
            for line in file:
                parts = line.strip().split(",")
                if len(parts) == 4:
                    expenses.append(
                        (parts[0], parts[1], parts[2], float(parts[3]))
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
        for name, category, date, amount in expenses:
            file.write(f"{name},{category},{date},{amount}\n")

    with open(BUDGET_FILE, "w") as file:
        file.write(str(budget))


def add_expense():
    try:
        name = input("Enter expense name: ")
        category = input("Enter category: ")
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter amount: "))

        if amount <= 0:
            print("Amount must be positive.")
            return

        expenses.append((name, category, date, amount))
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

    for name, category, date, amount in expenses:
        print(name, "-", amount)

    total = sum(amount for name, amount in expenses)
    print("Total Expenses:", total)
    print("Remaining Budget:", budget - total)


load_data()

while True:
    print("\n1. Add Expense")
    print("2. Set Budget")
    print("3. View Records")
    print("4. Show Charts")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        set_budget()
    elif choice == "3":
        view_records()
    elif choice == "4":
        show_charts()
    elif choice == "5":
        save_data()
        print("Data saved. Exiting program.")
        break
    else:
        print("Invalid choice.")
