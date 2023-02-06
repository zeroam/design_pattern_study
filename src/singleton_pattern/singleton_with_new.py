class Singleton:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance


if __name__ == "__main__":
    s = Singleton()
    print("Object created", s)

    s1 = Singleton()
    print("Object created", s1)
