import json
import os

FILE = "expenses.json"


def load_expenses():
    if os.path.exists(FILE):
        with open(FILE, "r") as file:
            return json.load(file)
    return []


def save_expenses(expenses):
    with open(FILE, "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense(expenses):
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    note = input("Enter note: ")

    expense = {
        "category": category,
        "amount": amount,
        "note": note
    }

    expenses.append(expense)
    save_expenses(expenses)

    print("\nExpense added successfully!")


def view_expenses(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    print("\n--- All Expenses ---")

    total = 0

    for i, expense in enumerate(expenses, 1):
        print(
            f"{i}. {expense['category']} - "
            f"₹{expense['amount']:.2f} - "
            f"{expense['note']}"
        )
        total += expense["amount"]

    print(f"\nTotal Expense: ₹{total:.2f}")


def category_summary(expenses):
    if not expenses:
        print("\nNo expenses found.")
        return

    summary = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    print("\n--- Category Summary ---")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount:.2f}")


def main():
    expenses = load_expenses()

    while True:
        print("\n==============================")
        print("      STUDENT EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_expense(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            category_summary(expenses)

        elif choice == "4":
            print("\nThank you for using Student Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    main()