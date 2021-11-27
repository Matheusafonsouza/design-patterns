from abc import ABC, abstractmethod

# abstract taxes
class ConditionalTaxTemplate(ABC):
    def calculate(self, budget):
        if self.should_max_tax(budget):
            return self.max_tax(budget)
        return self.min_tax(budget)

    @abstractmethod
    def should_max_tax(self):
        pass

    @abstractmethod
    def max_tax(self):
        pass

    @abstractmethod
    def min_tax(self):
        pass

# base classes
def IPVX(func):
    def wrapper(self, budget):
        return func(self, budget) + 50.0
    return wrapper

class ICMS:
    @IPVX
    def calculate(self, budget):
        return budget.amount * 0.1

class ISS:
    def calculate(self, budget):
        return budget.amount * 0.6


# conditional taxes
class ICPP(ConditionalTaxTemplate):
    def should_max_tax(self, budget):
        return budget.amount > 500

    def max_tax(self, budget):
        return budget.amount * 0.07

    def min_tax(self, budget):
        return budget.amount * 0.05

class IKCV(ConditionalTaxTemplate):
    def should_max_tax(self, budget):
        return budget.amount > 500 and any(
            budget.amount > 100 for budget in budget.get_items())

    def max_tax(self, budget):
        return budget.amount * 0.1

    def min_tax(self, budget):
        return budget.amount * 0.06
