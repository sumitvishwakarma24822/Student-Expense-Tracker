from expense_manager import ExpenseManager


def test_add_expense():
    manager = ExpenseManager()

    success, message = manager.add_expense(
        "Food",
        "100",
        "Lunch"
    )

    assert success is True
    assert message == "Expense added successfully."


def test_invalid_amount():
    manager = ExpenseManager()

    success, message = manager.add_expense(
        "Food",
        "-50",
        "Invalid expense"
    )

    assert success is False


def test_empty_category():
    manager = ExpenseManager()

    success, message = manager.add_expense(
        "",
        "100",
        "Test"
    )

    assert success is False
    