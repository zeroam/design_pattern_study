from typing import Protocol

from pizza import CheesePizza, ClamPizza, PepperoniPizza, Pizza, VeggiePizza


class PizzaFactory(Protocol):
    def create_pizza(self, type_: str) -> Pizza:
        ...


class NYPizzaFactory(PizzaFactory):
    def create_pizza(self, type_: str) -> Pizza:
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


class ChicagoPizzaFactory(PizzaFactory):
    def create_pizza(self, type_: str) -> Pizza:
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
    def __init__(self, factory: PizzaFactory) -> None:
        self.factory = factory

    def order_pizza(self, type_: str) -> Pizza:
        pizza = self.factory.create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class AbnormalPizzaStore:
    """잘못된 피자 스토어"""

    def __init__(self, factory: PizzaFactory) -> None:
        self.factory = factory

    def order_pizza(self, type_: str) -> Pizza:
        pizza = self.factory.create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        # pizza.cut()  # 피자를 잘라주지 않음
        pizza.box()

        return pizza


if __name__ == "__main__":
    factory = NYPizzaFactory()
    store = AbnormalPizzaStore(factory=factory)

    store.order_pizza("cheese")
