from expense_manager import ExpenseManager
from reports import display_expenses, display_summary


def main():
    manager = ExpenseManager()

    while True:
        print("\n==============================")
        print("      STUDENT EXPENSE TRACKER")
        print("==============================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Category Summary")
        print("4. Delete Expense")
        print("5. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            category = input("Enter category: ")
            amount = input("Enter amount: ")
            note = input("Enter note: ")

            success, message = manager.add_expense(
                category,
                amount,
                note
            )

            print(message)

        elif choice == "2":
            display_expenses(manager.get_expenses())

        elif choice == "3":
            display_summary(manager.get_expenses())

        elif choice == "4":
            display_expenses(manager.get_expenses())

            if manager.get_expenses():
                try:
                    number = int(input("\nEnter expense number to delete: "))
                    success, message = manager.delete_expense(number - 1)
                    print(message)
                except ValueError:
                    print("Please enter a valid number.")

        elif choice == "5":
            print("\nThank you for using Student Expense Tracker!")
            break

        else:
            print("\nInvalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
    