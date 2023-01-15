from pizza import CheesePizza, ClamPizza, PepperoniPizza, Pizza, VeggiePizza


class PizzaStore:
    def order_pizza(self, type_: str) -> Pizza:
        pizza: Pizza

        if type_ == "cheese":
            pizza = CheesePizza()
        elif type_ == "clam":
            pizza = ClamPizza()
        elif type_ == "pepperoni":
            pizza = PepperoniPizza()
        elif type_ == "veggie":
            pizza = VeggiePizza()
        else:
            raise ValueError(f"type: {type_} is not valid value")

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza
