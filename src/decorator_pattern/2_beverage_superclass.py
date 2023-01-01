from abc import ABC


class Beverage(ABC):
    _description: str = "음료"
    _milk: float = 0.2
    _soy: float = 0.1
    _mocha: float = 0.15
    _whip: float = 0.12

    _has_milk: bool = False
    _has_soy: bool = False
    _has_mocha: bool = False
    _has_whip: bool = False

    def get_description(self) -> str:
        return self._description

    def has_milk(self) -> bool:
        return self._has_milk

    def set_milk(self, status: bool):
        self._has_milk = status

    def has_soy(self) -> bool:
        return self._has_soy

    def set_soy(self, status: bool):
        self._has_soy = status

    def has_mocha(self) -> bool:
        return self._has_mocha

    def set_mocha(self, status: bool):
        self._has_mocha = status

    def has_whip(self) -> bool:
        return self._has_whip

    def set_whip(self, status: bool):
        self._has_whip = status

    def cost(self) -> float:
        total = 0.0
        if self.has_milk():
            total += self._milk
        if self.has_soy():
            total += self._soy
        if self.has_mocha():
            total += self._mocha
        if self.has_whip():
            total += self._whip

        return total


class DarkRoast(Beverage):
    _description = "DarkRoast"
    _coffee: float = 0.4

    def cost(self) -> float:
        return super().cost() + self._coffee
