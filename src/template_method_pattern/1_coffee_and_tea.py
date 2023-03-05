class Coffee:
    def prepareRecipe(self):
        self.boilWater()
        self.brewCoffeeGrinds()
        self.pourInCup()
        self.addSugarAndMilk()

    def boilWater(self):
        print("Boiling water")

    def brewCoffeeGrinds(self):
        print("Dripping Coffee through filter")

    def pourInCup(self):
        print("Pouring into cup")

    def addSugarAndMilk(self):
        print("Adding Sugar and Milk")


class Tea:
    def prepareRecipe(self):
        self.boilWater()
        self.steepTeaBag()
        self.pourInCup()
        self.addLemon()

    def boilWater(self):
        print("Boiling water")

    def steepTeaBag(self):
        print("Steeping the tea")

    def pourInCup(self):
        print("Pouring into cup")

    def addLemon(self):
        print("Adding Lemon")


if __name__ == "__main__":
    coffee = Coffee()
    coffee.prepareRecipe()

    tea = Tea()
    tea.prepareRecipe()
