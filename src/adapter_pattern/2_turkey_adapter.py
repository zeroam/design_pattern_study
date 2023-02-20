from lib import Duck, MallardDuck, Turkey, WildTurkey


class TurkeyAdapter(Duck):
    def __init__(self, turkey: Turkey) -> None:
        self.turkey = turkey

    def quack(self) -> None:
        self.turkey.gobble()

    def fly(self) -> None:
        for _ in range(5):
            self.turkey.fly()


def play_with_duck(duck: Duck):
    print("hello duck")
    duck.quack()

    print("fly duck")
    duck.fly()


if __name__ == "__main__":
    duck = MallardDuck()
    play_with_duck(duck)

    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)
    play_with_duck(turkey_adapter)
