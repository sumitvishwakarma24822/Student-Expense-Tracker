class Expense:
    def __init__(self, category, amount, note):
        self.category = category
        self.amount = amount
        self.note = note

    def to_dict(self):
        return {
            "category": self.category,
            "amount": self.amount,
            "note": self.note
        }

    @staticmethod
    def from_dict(data):
        return Expense(
            data["category"],
            data["amount"],
            data["note"]
        )