class Item:
    """ЗАДАЧА: Сравнение товаров по цене через __lt__ и по всем полям через __eq__"""
    def __init__(self, name, price): self.name, self.price = name, price
    def __lt__(self, other):
        return int(self.price) < int(other.price)
        pass
    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.name == other.name and self.price == other.price
        pass