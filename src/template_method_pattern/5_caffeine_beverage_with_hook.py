from abc import ABC, abstractmethod


class CaffeineBeverage(ABC):
    def prepareRecipe(self):
        self.boilWater()
        self.brew()
        self.pourInCup()
        if self.customerWantsCondiments():
            self.addCondiments()

    def boilWater(self):
        print("Boiling water")

    def pourInCup(self):
        print("Pouring into cup")

    def customerWantsCondiments(self):
        return True

    @abstractmethod
    def brew(self):
        pass

    @abstractmethod
    def addCondiments(self):
        pass


class CoffeeWithHook(CaffeineBeverage):
    def brew(self):
        print("Dripping Coffee through filter")

    def addCondiments(self):
        print("Adding Sugar and Milk")

    def customerWantsCondiments(self):
        answer = self.getUserInput()

        if answer.lower().startswith("y"):
            return True
        else:
            return False

    def getUserInput(self):
        answer = None

        print("Would you like milk and sugar with your coffee (y/n)? ", end="")
        answer = input()

        if answer == "":
            return "no"

        return answer


class TeaWithHook(CaffeineBeverage):
    def brew(self):
        print("Steeping the tea")

    def addCondiments(self):
        print("Adding Lemon")

    def customerWantsCondiments(self):
        answer = self.getUserInput()

        if answer.lower().startswith("y"):
            return True
        else:
            return False

    def getUserInput(self):
        answer = None

        print("Would you like lemon with your tea (y/n)? ", end="")
        answer = input()

        if answer == "":
            return "no"

        return answer


if __name__ == "__main__":
    coffee = CoffeeWithHook()
    coffee.prepareRecipe()

    tea = TeaWithHook()
    tea.prepareRecipe()
