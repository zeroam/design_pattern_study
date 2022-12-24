from abc import ABC, abstractmethod
from typing import Protocol, runtime_checkable


class Duck(ABC):
    @abstractmethod
    def display(self):
        ...

    def swim(self):
        print("swimming")


@runtime_checkable
class Flyable(Protocol):
    def fly(self):
        ...


@runtime_checkable
class Quackable(Protocol):
    def quack(self):
        ...


class MallardDuck(Duck, Flyable, Quackable):
    def display(self):
        print("Mallard Duck")

    def fly(self):
        print("flying")

    def quack(self):
        print("quack")


class RedheadDuck(Duck, Flyable, Quackable):
    def display(self):
        print("RedheadDuck")

    def fly(self):
        print("flying")

    def quack(self):
        print("quack")


class RubberDuck(Duck, Quackable):
    def display(self):
        print("RubberDuck")

    def quack(self):
        print("bbick bbick")


class DecoyDuck(Duck):
    def display(self):
        print("DecoyDuck")


def main():
    duck: Duck = RedheadDuck()

    print(duck.__class__.__name__)
    print("- display:", end=" ")
    duck.display()
    if isinstance(duck, Quackable):
        print("- quack:", end=" ")
        duck.quack()
    if isinstance(duck, Flyable):
        print("- fly:", end=" ")
        duck.fly()


if __name__ == "__main__":
    main()
