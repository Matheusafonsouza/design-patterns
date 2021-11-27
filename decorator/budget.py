class Budget:
    def __init__(self):
        self._items = list()

    @property
    def amount(self):
        return sum([item.amount for item in self._items])
    
    def get_items(self):
        return tuple(self._items)

    @property
    def total_items(self):
        return len(self._items)

    def add_item(self, item):
        self._items.append(item)

class Item:
    def __init__(self, name, amount):
        self._name = name
        self._amount = amount

    @property
    def amount(self):
        return self._amount

    @property
    def name(self):
        return self._name