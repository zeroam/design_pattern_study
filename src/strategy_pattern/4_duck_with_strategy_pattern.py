from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


class Duck(ABC):
    fly_behavior: FlyBehavior
    quack_behavior: QuackBehavior

    @abstractmethod
    def display(self):
        ...

    def swim(self):
        print("swimming")

    def set_fly_behavior(self, fly_behavior: FlyBehavior):
        self.fly_behavior = fly_behavior

    def set_quack_behavior(self, quack_behavior: QuackBehavior):
        self.quack_behavior = quack_behavior

    def perform_fly(self):
        self.fly_behavior.fly()

    def perform_quack(self):
        self.quack_behavior.quack()


@runtime_checkable
class FlyBehavior(Protocol):
    def fly(self):
        ...


class FlyWithWings(FlyBehavior):
    def fly(self):
        print("fly")


class FlyNoWay(FlyBehavior):
    def fly(self):
        print("no fly")


class FlyRocketPowered(FlyBehavior):
    def fly(self):
        print("fly rocket powered")


@runtime_checkable
class QuackBehavior(Protocol):
    def quack(self):
        ...


class Quack(QuackBehavior):
    def quack(self):
        print("quack")


class Squack(QuackBehavior):
    def quack(self):
        print("squack")


class MuteQuack(QuackBehavior):
    def quack(self):
        print("mute quack")


class MallardDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("Mallard Duck")


class RedheadDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyWithWings()
        self.quack_behavior = Quack()

    def display(self):
        print("RedheadDuck")


class RubberDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = Squack()

    def display(self):
        print("RubberDuck")


class DecoyDuck(Duck):
    def __init__(self) -> None:
        self.fly_behavior = FlyNoWay()
        self.quack_behavior = MuteQuack()

    def display(self):
        print("DecoyDuck")


def main():
    duck: Duck = DecoyDuck()

    print(duck.__class__.__name__)
    print("- display:", end=" ")
    duck.display()
    print("- quack:", end=" ")
    duck.perform_quack()
    print("- fly:", end=" ")
    duck.perform_fly()

    duck.set_fly_behavior(FlyRocketPowered())
    print("- changed fly:", end=" ")
    duck.perform_fly()


if __name__ == "__main__":
    main()
