from pizza import CheesePizza, ClamPizza, PepperoniPizza, Pizza, VeggiePizza


class SimplePizzaFactory:
    @staticmethod
    def create_pizza(type_: str) -> Pizza:
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

        return pizza


class PizzaStore:
    factory: type[SimplePizzaFactory] = SimplePizzaFactory

    def order_pizza(self, type_: str) -> Pizza:
        pizza = self.factory.create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


if __name__ == "__main__":
    store = PizzaStore()

    store.order_pizza("cheese")
