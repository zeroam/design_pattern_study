from abc import ABC


class Pizza(ABC):
    name: str

    def prepare(self):
        print(f"prepare {self.name}")

    def bake(self):
        print(f"bake {self.name}")

    def cut(self):
        print(f"cut {self.name}")

    def box(self):
        print(f"box {self.name}")


class CheesePizza(Pizza):
    name = "Cheese Pizza"


class NYCheesePizza(Pizza):
    name = "NewYork Cheese Pizza"


class ChicagoCheesePizza(Pizza):
    name = "Chicago Cheese Pizza"


class VeggiePizza(Pizza):
    name = "Veggie Pizza"


class NYVeggiePizza(Pizza):
    name = "NewYork Veggie Pizza"


class ChicagoVeggiePizza(Pizza):
    name = "Chicago Veggie Pizza"


class ClamPizza(Pizza):
    name = "Clam Pizza"


class NYClamPizza(Pizza):
    name = "NewYork Clam Pizza"


class ChicagoClamPizza(Pizza):
    name = "Chicago Clam Pizza"


class PepperoniPizza(Pizza):
    name = "Pepperoni Pizza"


class NYPepperoniPizza(Pizza):
    name = "NewYork Pepperoni Pizza"


class ChicagoPepperoniPizza(Pizza):
    name = "Chicago Pepperoni Pizza"
