from abc import ABC, abstractmethod


class BasePizza(ABC):
    """
    Abstract Base class for all type of pizzas
    """

    @abstractmethod
    def get_price(self):
        pass


class Margherita(BasePizza):
    PRICE = 30

    def get_price(self):
        return Margherita.PRICE


class VeggieDelight(BasePizza):
    PRICE = 60

    def get_price(self):
        return VeggieDelight.PRICE


class Mexican(BasePizza):
    PRICE = 100

    def get_price(self):
        return Mexican.PRICE
