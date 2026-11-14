import matplotlib.pyplot as plt


def plot_all_charts(category_totals, monthly_totals, budgets):
    
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(18, 5))

    # Chart 1, category-wise spending
    ax1.bar(list(category_totals.keys()), list(category_totals.values()), color="steelblue")
    ax1.set_title("Category-wise Spending")
    ax1.set_xlabel("Category")
    ax1.set_ylabel("Amount (Rs.)")
    ax1.tick_params(axis="x", rotation=30)

    # Chart 2, monthly expenditure
    ax2.plot(list(monthly_totals.keys()), list(monthly_totals.values()), marker="o", color="darkorange")
    ax2.set_title("Monthly Expenditure")
    ax2.set_xlabel("Month")
    ax2.set_ylabel("Amount (Rs.)")

    # Chart 3, budget vs actual (every category from either source)
    categories = sorted(set(budgets) | set(category_totals))
    x = range(len(categories))
    width = 0.4
    ax3.bar([i - width / 2 for i in x], [budgets.get(c, 0) for c in categories],
            width, label="Budget", color="lightgray")
    ax3.bar([i + width / 2 for i in x], [category_totals.get(c, 0) for c in categories],
            width, label="Actual", color="tomato")
    ax3.set_xticks(list(x))
    ax3.set_xticklabels(categories, rotation=30)
    ax3.set_title("Budget vs Actual Spending")
    ax3.set_xlabel("Category")
    ax3.set_ylabel("Amount (Rs.)")
    ax3.legend()

    plt.tight_layout()
    plt.show()  