from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        self.addCondiments()

    def boilWater(self):
        print("Boiling water")

    def pourInCup(self):
        print("Pouring into cup")

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def addCondiments(self):
        pass


class Coffee(CaffeineBeverage):
    def brew(self):
        print("Dripping Coffee through filter")

    def addCondiments(self):
        print("Adding Sugar and Milk")


class Tea(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea")

    def addCondiments(self):
        print("Adding Lemon")


if __name__ == "__main__":
    coffee = Coffee()
    coffee.prepareRecipe()

    tea = Tea()
    tea.prepareRecipe()
