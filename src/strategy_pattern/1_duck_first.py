from abc import ABC, abstractmethod


class Duck(ABC):
    @abstractmethod
    def display(self):
        ...

    def quack(self):
        print("quack")

    def swim(self):
        print("swimming")


class MallardDuck(Duck):
    def display(self):
        print("Mallard Duck")


class RedheadDuck(Duck):
    def display(self):
        print("RedheadDuck")


def main():
    duck: Duck = MallardDuck()

    print(duck.__class__.__name__)
    print("- display:", end=" ")
    duck.display()
    print("- quack:", end=" ")
    duck.quack()


if __name__ == "__main__":
    main()
