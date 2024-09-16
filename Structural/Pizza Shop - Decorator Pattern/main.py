from pizza import Margherita, VeggieDelight, Mexican
from extras import ExtraToppings, ExtraCheese

if __name__ == "__main__":
    margherita = Margherita()
    veggie_delight = VeggieDelight()
    mexican = Mexican()

    margherita = ExtraToppings(margherita)
    veggie_delight = ExtraToppings(ExtraCheese(veggie_delight))
    mexican = ExtraCheese(mexican)

    print(margherita.get_price())
    print(veggie_delight.get_price())
    print(mexican.get_price())
