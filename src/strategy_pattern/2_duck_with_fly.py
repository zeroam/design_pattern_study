from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def display(self):
        ...

    def quack(self):
        print("quack")

    def swim(self):
        print("swimming")

    def fly(self):
        print("flying")


class MallardDuck(Duck):
    def display(self):
        print("Mallard Duck")


class RedheadDuck(Duck):
    def display(self):
        print("RedheadDuck")


class RubberDuck(Duck):
    def display(self):
        print("RubberDuck")

    def quack(self):
        print("bbick bbick")

    def fly(self):
        print("nothing")


class DecoyDuck(Duck):
    def display(self):
        print("DecoyDuck")

    def quack(self):
        print("nothing")

    def fly(self):
        print("nothing")


def main():
    duck: Duck = DecoyDuck()

    print(duck.__class__.__name__)
    print("- display:", end=" ")
    duck.display()
    print("- quack:", end=" ")
    duck.quack()
    print("- fly:", end=" ")
    duck.fly()


if __name__ == "__main__":
    main()
