from abc import ABC, abstractmethod


class Beverage(ABC):
    _description: str = "음료"

    def get_description(self) -> str:
        return self._description

    @abstractmethod
    def cost(self) -> float:
        ...


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


class HouseBlendWithSteamMilkAndMocha(HouseBlend):
    _description: str = "House Blend, steam milk, mocha"

    _milk: float = 0.2
    _mocha: float = 0.1

    def cost(self) -> float:
        return super().cost() + self._milk + self._mocha


class DarkRoastWithSteamMilk(DarkRoast):
    _description: str = "Dark Roast, steam milk"

    _milk: float = 0.2

    def cost(self) -> float:
        return super().cost() + self._milk
