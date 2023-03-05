from abc import ABC, abstractmethod


class AbstractClass(ABC):
    @abstractmethod
    def primitiveOperation1(self):
        pass

    @abstractmethod
    def primitiveOperation2(self):
        pass

    def templateMethod(self):
        self.primitiveOperation1()
        self.primitiveOperation2()


class ConcreteClass(AbstractClass):
    def primitiveOperation1(self):
        print("primitiveOperation1")

    def primitiveOperation2(self):
        print("primitiveOperation2")


if __name__ == "__main__":
    concreteClass = ConcreteClass()
    concreteClass.templateMethod()
