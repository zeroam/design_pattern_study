from typing import Protocol


class Duck(Protocol):
    def quack(self) -> None:
        ...

    def fly(self) -> None:
        ...


class Turkey(Protocol):
    def gobble(self) -> None:
        ...

    def fly(self) -> None:
        ...


class MallardDuck(Duck):
    def quack(self) -> None:
        print("quack")

    def fly(self) -> None:
        print("flying")


class WildTurkey(Turkey):
    def gobble(self) -> None:
        print("gobble")

    def fly(self) -> None:
        print("flying short")
