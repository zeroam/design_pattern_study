from abc import ABC, abstractmethod

from pizza import (
    ChicagoCheesePizza,
    ChicagoClamPizza,
    ChicagoPepperoniPizza,
    ChicagoVeggiePizza,
    NYCheesePizza,
    NYClamPizza,
    NYPepperoniPizza,
    NYVeggiePizza,
    Pizza,
)


class PizzaStore(ABC):
    def order_pizza(self, type_: str) -> Pizza:
        pizza: Pizza = self.create_pizza(type_)

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza

    @abstractmethod
    def create_pizza(self, type_: str) -> Pizza:
        ...


class NYPizzaStore(PizzaStore):
    def create_pizza(self, type_: str) -> Pizza:
        pizza: Pizza

        if type_ == "cheese":
            pizza = NYCheesePizza()
        elif type_ == "clam":
            pizza = NYClamPizza()
        elif type_ == "pepperoni":
            pizza = NYPepperoniPizza()
        elif type_ == "veggie":
            pizza = NYVeggiePizza()
        else:
            raise ValueError(f"type: {type_} is not valid value")

        return pizza


class ChicagoPizzaStore(PizzaStore):
    def create_pizza(self, type_: str) -> Pizza:
        pizza: Pizza

        if type_ == "cheese":
            pizza = ChicagoCheesePizza()
        elif type_ == "clam":
            pizza = ChicagoClamPizza()
        elif type_ == "pepperoni":
            pizza = ChicagoPepperoniPizza()
        elif type_ == "veggie":
            pizza = ChicagoVeggiePizza()
        else:
            raise ValueError(f"type: {type_} is not valid value")

        return pizza


if __name__ == "__main__":
    store = NYPizzaStore()

    store.order_pizza("cheese")
