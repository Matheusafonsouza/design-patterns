from budget import Budget
from taxes import ICMS, ISS

class TaxCalculator:
    def make_calc(self, budget, tax_calculator):
        calculated_tax = tax_calculator.calculate(budget)
        print(calculated_tax)

if __name__ == '__main__':
    budget = Budget(500)
    TaxCalculator().make_calc(budget, ISS())
    TaxCalculator().make_calc(budget, ICMS())