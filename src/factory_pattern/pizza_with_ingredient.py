from __future__ import annotations

from abc import ABC, abstractmethod
from collections.abc import Sequence
from typing import Protocol

"""
Interface
"""


class Dough(ABC):
    name: str


class Sauce(ABC):
    name: str


class Vegetable(ABC):
    name: str


class Cheese(ABC):
    name: str


class Pepperoni(ABC):
    name: str


class Clam(ABC):
    name: str


class PizzaIngredientFactory(Protocol):
    def create_dough(self) -> Dough:
        ...

    def create_sauce(self) -> Sauce:
        ...

    def create_cheese(self) -> Cheese:
        ...

    def create_veggies(self) -> Sequence[Vegetable]:
        ...

    def create_pepperoni(self) -> Pepperoni:
        ...

    def create_clam(self) -> Clam:
        ...


class Pizza(ABC):
    name: str
    dough: Dough
    sauce: Sauce
    veggies: list[Vegetable]
    cheese: Cheese
    pepperoni: Pepperoni
    clam: Clam

    @abstractmethod
    def prepare(self) -> None:
        ...

    def bake(self):
        print("bake pizza")

    def cut(self):
        print("cut pizza")

    def box(self):
        print("boxing pizza")


"""
Implement
"""


class ThinCrustDough(Dough):
    name = "ThinCrustDough"


class ThickCrustDough(Dough):
    name = "ThickCrustDough"


class MarinaraSauce(Sauce):
    name = "MarinaraSauce"


class PlumTomatoSauce(Sauce):
    name = "PlumTomatoSauce"


class ReggianoCheese(Cheese):
    name = "ReggianoCheese"


class MozzarellaCheese(Cheese):
    name = "MozzarellaCheese"


class Garlic(Vegetable):
    name = "Garlic"


class Onion(Vegetable):
    name = "Onion"


class Mushroom(Vegetable):
    name = "Mushroom"


class RedPepper(Vegetable):
    name = "RedPepper"


class EggPlant(Vegetable):
    name = "EggPlant"


class BlackOlives(Vegetable):
    name = "BlackOlives"


class Spinach(Vegetable):
    name = "Spinach"


class SlicedPepperoni(Pepperoni):
    name = "SlicedPepperoni"


class FreshClam(Clam):
    name = "FreshClam"


class FrozenClam(Clam):
    name = "FrozenClam"


class NYPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThinCrustDough()

    def create_sauce(self) -> Sauce:
        return MarinaraSauce()

    def create_cheese(self) -> Cheese:
        return ReggianoCheese()

    def create_veggies(self) -> Sequence[Vegetable]:
        return (Garlic(), Onion(), Mushroom(), RedPepper())

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clam:
        return FreshClam()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):
    def create_dough(self) -> Dough:
        return ThickCrustDough()

    def create_sauce(self) -> Sauce:
        return PlumTomatoSauce()

    def create_cheese(self) -> Cheese:
        return MozzarellaCheese()

    def create_veggies(self) -> Sequence[Vegetable]:
        return (EggPlant(), Spinach(), BlackOlives())

    def create_pepperoni(self) -> Pepperoni:
        return SlicedPepperoni()

    def create_clam(self) -> Clam:
        return FrozenClam()


class CheesePizza(Pizza):
    ingredient_factory: PizzaIngredientFactory

    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Preparing CheesePizza...")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()


class ClamPizza(Pizza):
    ingredient_factory: PizzaIngredientFactory

    def __init__(self, ingredient_factory: PizzaIngredientFactory) -> None:
        self.ingredient_factory = ingredient_factory

    def prepare(self) -> None:
        print("Preparing ClamPizza...")
        self.dough = self.ingredient_factory.create_dough()
        self.sauce = self.ingredient_factory.create_sauce()
        self.cheese = self.ingredient_factory.create_cheese()
        self.clam = self.ingredient_factory.create_clam()
