class DiscountItems:
    def __init__(self, next_discount=None):
        self._next_discount = next_discount

    def calculate(self, budget):
        if budget.total_items > 5:
            return budget.amount * 0.1
        elif self._next_discount:
            return self._next_discount.calculate(budget)
        return 0

class DiscountAmount:
    def __init__(self, next_discount=None):
        self._next_discount = next_discount
        
    def calculate(self, budget):
        if budget.amount > 500:
            return budget.amount * 0.6
        elif self._next_discount:
            return self._next_discount.calculate(budget)
        return 0