from budget import Budget, Item
from discounts import DiscountAmount, DiscountItems

class DiscountCalculator:
    def calculate(self, budget):
        return DiscountAmount(DiscountItems).calculate(budget)

if __name__ == '__main__':
    budget = Budget()

    budget.add_item(Item('item1', 100))
    budget.add_item(Item('item1', 50))
    budget.add_item(Item('item1', 400))

    discount = DiscountCalculator().calculate(budget)
    print(discount)