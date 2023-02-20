from lib import Duck, MallardDuck, WildTurkey


def play_with_duck(duck: Duck):
    print("hello duck")
    duck.quack()

    print("fly duck")
    duck.fly()


if __name__ == "__main__":
    duck = MallardDuck()
    play_with_duck(duck)

    turkey = WildTurkey()
    # play_with_duck(turkey)  # error
