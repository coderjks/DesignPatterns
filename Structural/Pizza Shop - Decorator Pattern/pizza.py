from abc import ABC, abstractmethod


class BasePizza(ABC):
    """
    Abstract Base class for all type of pizzas
    """

    def __init__(self, price):
        self.base_price = price

    @abstractmethod
    def get_price(self):
        return self.base_price


class Margherita(BasePizza):
    PRICE = 30

    def __init(self, price):
        super().__init__(price)

    def get_price(self):
        return self.base_price + Margherita.PRICE


class VeggieDelight(BasePizza):
    PRICE = 60

    def __init(self, price):
        super().__init__(price)

    def get_price(self):
        return self.base_price + VeggieDelight.PRICE


class Mexican(BasePizza):
    PRICE = 100

    def __init(self, price):
        super().__init__(price)

    def get_price(self):
        return self.base_price + Mexican.PRICE
