from lib import Duck, MallardDuck, WildTurkey


class WildTurkeyAdapter(WildTurkey, Duck):
    def quack(self) -> None:
        self.gobble()

    def fly(self) -> None:
        for _ in range(5):
            super().fly()


def play_with_duck(duck: Duck):
    print("hello duck")
    duck.quack()

    print("fly duck")
    duck.fly()


if __name__ == "__main__":
    duck = MallardDuck()
    play_with_duck(duck)

    turkey_adapter = WildTurkeyAdapter()
    play_with_duck(turkey_adapter)
