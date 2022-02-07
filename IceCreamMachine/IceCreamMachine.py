#This test was provided by Test Dome as a Python employment test
#Test was acquired here: https://app.testdome.com/t?GeneratorId=46
#Implement the IceCreamMachine's scoops method so that it returns all
#combinations of one ingredient and one topping. If there are no ingredients or
#toppings, the method should return an empty list.
#For example IceCreamMachine([vanilla, chocolate}, [chocolate
#sauce]).scoops() should return [[vanilla, chocolate sauce],[chocolate, chocolatesauce]].

class IceCreamMachine:

    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        #create the list
        scoop = []
        #create list to add into list for the correct format
        addscoop = []
        for i in range(len(self.ingredients)):
            for j in range(len(self.toppings)):
                addscoop += [self.ingredients[i], self.toppings[j]]
                scoop.append(addscoop)
                addscoop = []

        return scoop


if __name__ == "__main__":
    machine = IceCreamMachine(["vanilla", "strawberry", "chocolate", "pistachio"], ["sprinkles","cookie crumbles"])
    print(machine.scoops())
    # should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]