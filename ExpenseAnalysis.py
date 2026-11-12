from collections import defaultdict
from datetime import datetime

from BudgetManagement import cal_total_expenses


def category_spending(expenses):
    """Total spent per category, as a dictionary {category: amount}."""
    totals = defaultdict(float)
    for e in expenses:
        totals[e.category] += e.calculate_amount()
    return dict(totals)


def highest_expenses(expenses, n=3):
    """Return the n largest individual expenses, sorted from highest to lowest."""
    return sorted(expenses, key=lambda e: e.calculate_amount(), reverse=True)[:n]


def monthly_spending(expenses):
    """Total spent per month, as a dictionary {'YYYY-MM': amount}, sorted by month."""
    totals = defaultdict(float)
    for e in expenses:
        month = datetime.strptime(e.date, "%Y-%m-%d").strftime("%Y-%m")
        totals[month] += e.calculate_amount()
    return dict(sorted(totals.items()))


def budget_comparison(expenses, budget):
    """Compare actual spending with the budget."""
    spent = cal_total_expenses(expenses)
    return {
        "budget": budget,
        "spent": spent,
        "remaining": budget - spent,
        "percent_used": (spent / budget * 100) if budget > 0 else 0.0,
        "over_budget": spent > budget,
    }


def summary_report(expenses, budget):
    """Print a full report: category totals, top expenses, monthly totals, budget status."""
    print("\n===== EXPENSE SUMMARY REPORT =====")

    print("\nCategory-wise spending:")
    categories = category_spending(expenses)
    if not categories:
        print("  No expenses recorded.")
    for category, amount in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {category:<15} {amount:>10.2f}")

    print("\nHighest expenses:")
    for e in highest_expenses(expenses):
        print(f"  {e.description:<15} {e.calculate_amount():>10.2f}  ({e.category}, {e.date})")

    print("\nMonthly spending:")
    for month, amount in monthly_spending(expenses).items():
        print(f"  {month:<15} {amount:>10.2f}")

    c = budget_comparison(expenses, budget)
    print("\nBudget vs Actual:")
    print(f"  Budget:    {c['budget']:.2f}")
    print(f"  Spent:     {c['spent']:.2f}")
    print(f"  Remaining: {c['remaining']:.2f}")
    print(f"  Used:      {c['percent_used']:.1f}%")
    if c["over_budget"]:
        print("  WARNING: You are over budget!")