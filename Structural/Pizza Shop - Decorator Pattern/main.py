from pizza import Margherita, VeggieDelight, Mexican
from extras import ExtraToppings, ExtraCheese

if __name__ == "__main__":
    margherita = Margherita(100)
    veggie_delight = VeggieDelight(150)
    mexican = Mexican(400)

    margherita = ExtraToppings(margherita)
    veggie_delight = ExtraToppings(ExtraCheese(veggie_delight))
    mexican = ExtraCheese(mexican)

    print(margherita.get_price())
    print(veggie_delight.get_price())
    print(mexican.get_price())
