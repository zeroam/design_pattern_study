from abc import ABC, abstractmethod


class Beverage(ABC):
    _description: str = "음료"

    def get_description(self) -> str:
        return self._description

    @abstractmethod
    def cost(self) -> float:
        ...


class CondimentDecorator(Beverage, ABC):
    _beverage: Beverage

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage


class Milk(CondimentDecorator):
    _milk: float = 0.2

    def cost(self) -> float:
        return self._beverage.cost() + self._milk

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Milk"


class Mocha(CondimentDecorator):
    _mocha: float = 0.1

    def cost(self) -> float:
        return self._beverage.cost() + self._mocha

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"


class Soy(CondimentDecorator):
    _soy: float = 0.12

    def cost(self) -> float:
        return self._beverage.cost() + self._soy

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soy"


class Whip(CondimentDecorator):
    _whip: float = 0.13

    def cost(self) -> float:
        return self._beverage.cost() + self._whip

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Whip"


class HouseBlend(Beverage):
    _description: str = "HouseBlend"

    def cost(self) -> float:
        return 4.5


class DarkRoast(Beverage):
    _description: str = "DarkRoast"

    def cost(self) -> float:
        return 4.2


class Decaf(Beverage):
    _description: str = "Decaf"

    def cost(self) -> float:
        return 4.5


class Espresso(Beverage):
    _description: str = "Espresso"

    def cost(self) -> float:
        return 5.0


if __name__ == "__main__":
    house_blend = HouseBlend()
    print(f"{house_blend.get_description()}: ${house_blend.cost()}")

    house_blend_with_mocha = Mocha(house_blend)
    print(f"{house_blend_with_mocha.get_description()}: ${house_blend_with_mocha.cost()}")

    house_blend_with_mocha_and_whip = Whip(Mocha(house_blend))
    print(f"{house_blend_with_mocha_and_whip.get_description()}: ${house_blend_with_mocha_and_whip.cost()}")
