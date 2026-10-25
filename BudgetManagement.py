
def validate_amount(amount):
	try:
		value = float(amount)
	except (TypeError, ValueError) as error:
		raise ValueError("Amount must be a valid number") 
	if value < 0:
		raise ValueError("Amount cannot be negative")
	return value


def add_transaction(transactions, description, amount):
	value = validate_amount(amount)
	if not description or not str(description).strip():
		raise ValueError("Transaction description cannot be empty")
	transactions.append({"description": str(description).strip(), "amount": value})


def cal_total_expenses(transactions):
	return sum(validate_amount(transaction["amount"]) for transaction in transactions)


def cal_remaining_budget(budget, transactions):
	return validate_amount(budget) - cal_total_expenses(transactions)


if __name__ == "__main__":
	transactions = []
	try:
		budget = validate_amount(input("Enter your budget: $"))
		while True:
			description = input("Expense description (or blank to finish): ").strip()
			if not description:
				break
			amount = validate_amount(input("Expense amount: ₹"))
			add_transaction(transactions, description, amount)

		print(f"Total expenses: ₹{cal_total_expenses(transactions):.2f}")
		print(f"Remaining budget: ₹{cal_remaining_budget(budget, transactions):.2f}")
	except (TypeError, ValueError) as error:
		raise ValueError(f"Invalid budget or transaction: {error}") 
