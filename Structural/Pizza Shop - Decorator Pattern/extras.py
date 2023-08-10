from pizza import BasePizza, ABC


class Extras(BasePizza, ABC):
    """
    Abstract Class for adding extra toppings/cheese etc.
    """


class ExtraToppings(Extras):
    PRICE = 70

    def __init__(self, base_pizza):
        self.base_pizza = base_pizza

    def get_price(self):
        return self.base_pizza.get_price() + ExtraToppings.PRICE


class ExtraCheese(Extras):
    PRICE = 150

    def __init__(self, base_pizza):
        self.base_pizza = base_pizza

    def get_price(self):
        return self.base_pizza.get_price() + ExtraCheese.PRICE
