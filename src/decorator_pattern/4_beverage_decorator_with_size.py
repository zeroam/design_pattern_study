from abc import ABC, abstractmethod
from enum import Enum


class SizeEnum(str, Enum):
    TALL = "tall"
    GRANDE = "grande"
    VENTI = "venti"


class Beverage(ABC):
    _description: str = "음료"
    _size: SizeEnum

    def __init__(self) -> None:
        self._size = SizeEnum.TALL

    def get_description(self) -> str:
        return self._description

    def get_size(self):
        return self._size

    def set_size(self, value: SizeEnum):
        self._size = value

    @abstractmethod
    def cost(self) -> float:
        ...


class CondimentDecorator(Beverage, ABC):
    _beverage: Beverage

    def __init__(self, beverage: Beverage) -> None:
        self._beverage = beverage
        super().__init__()


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


class Milk(CondimentDecorator):
    _milk: float = 0.2

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Milk"

    def cost(self) -> float:
        total = self._beverage.cost()
        if self._beverage.get_size() == SizeEnum.TALL:
            total += self._milk
        elif self._beverage.get_size() == SizeEnum.GRANDE:
            total += self._milk * 1.2
        elif self._beverage.get_size() == SizeEnum.VENTI:
            total += self._milk * 1.5

        return total


class Mocha(CondimentDecorator):
    _mocha: float = 0.1

    def cost(self) -> float:
        total = self._beverage.cost()
        if self._beverage.get_size() == SizeEnum.TALL:
            total += self._mocha
        elif self._beverage.get_size() == SizeEnum.GRANDE:
            total += self._mocha * 1.2
        elif self._beverage.get_size() == SizeEnum.VENTI:
            total += self._mocha * 1.5

        return total

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Mocha"


class Soy(CondimentDecorator):
    _soy: float = 0.12

    def cost(self) -> float:
        total = self._beverage.cost()
        if self._beverage.get_size() == SizeEnum.TALL:
            total += self._soy
        elif self._beverage.get_size() == SizeEnum.GRANDE:
            total += self._soy * 1.2
        elif self._beverage.get_size() == SizeEnum.VENTI:
            total += self._soy * 1.5

        return total

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Soy"


class Whip(CondimentDecorator):
    _whip: float = 0.13

    def cost(self) -> float:
        total = self._beverage.cost()
        if self._beverage.get_size() == SizeEnum.TALL:
            total += self._whip
        elif self._beverage.get_size() == SizeEnum.GRANDE:
            total += self._whip * 1.2
        elif self._beverage.get_size() == SizeEnum.VENTI:
            total += self._whip * 1.5

        return total

    def get_description(self) -> str:
        return self._beverage.get_description() + ", Whip"


if __name__ == "__main__":
    house_blend = HouseBlend()
    house_blend.set_size(SizeEnum.GRANDE)
    print(f"{house_blend.get_description()}: ${house_blend.cost()}")

    house_blend_with_mocha = Mocha(house_blend)
    print(f"{house_blend_with_mocha.get_description()}: ${house_blend_with_mocha.cost()}")

    house_blend_with_mocha_and_whip = Whip(Mocha(house_blend))
    print(f"{house_blend_with_mocha_and_whip.get_description()}: ${house_blend_with_mocha_and_whip.cost()}")
