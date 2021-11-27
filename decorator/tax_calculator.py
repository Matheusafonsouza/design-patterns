from budget import Budget, Item
from taxes import ICMS, ISS, ICPP, IKCV

class TaxCalculator:
    def make_calc(self, budget, tax_calculator):
        calculated_tax = tax_calculator.calculate(budget)
        print(calculated_tax)

if __name__ == '__main__':
    budget = Budget()

    budget.add_item(Item('item1', 50))
    budget.add_item(Item('item2', 200))
    budget.add_item(Item('item3', 250))

    print('ISS AND ICMS')
    TaxCalculator().make_calc(budget, ISS())
    TaxCalculator().make_calc(budget, ICMS())

    print('ICPP AND IKCV')
    TaxCalculator().make_calc(budget, ICPP())
    TaxCalculator().make_calc(budget, IKCV())