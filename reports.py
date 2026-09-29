def calculate_total(expenses):
    return sum(expense["amount"] for expense in expenses)


def category_summary(expenses):
    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category not in summary:
            summary[category] = 0

        summary[category] += amount

    return summary


def display_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n--- All Expenses ---")

    for number, expense in enumerate(expenses, 1):
        print(
            f"{number}. "
            f"{expense['category']} - "
            f"₹{expense['amount']:.2f} - "
            f"{expense['note']}"
        )

    print(f"\nTotal Expense: ₹{calculate_total(expenses):.2f}")


def display_summary(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    summary = category_summary(expenses)

    print("\n--- Category Summary ---")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")