def validate_category(category):
    return bool(category.strip())


def validate_amount(amount):
    try:
        value = float(amount)
        return value > 0
    except ValueError:
        return False