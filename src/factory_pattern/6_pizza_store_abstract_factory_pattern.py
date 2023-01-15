from abc import ABC, abstractmethod

from pizza_with_ingredient import (
    CheesePizza,
    ClamPizza,
    NYPizzaIngredientFactory,
    Pizza,
    PizzaIngredientFactory,
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
        ingredient_factory: PizzaIngredientFactory = NYPizzaIngredientFactory()

        if type_ == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.name = "New York Style Cheese Pizza"
        elif type_ == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.name = "New York Style Clam Pizza"
        else:
            raise ValueError(f"type: {type_} is not valid value")

        return pizza


if __name__ == "__main__":
    store = NYPizzaStore()

    store.order_pizza("cheese")
