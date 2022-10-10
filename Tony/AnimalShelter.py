from Animal import Animal

class AnimalShelter:
    def __init__(self):
        self.dict = {}

    def addAnimal(self, animal):
        if animal.species in self.dict:
            self.dict[animal.species].append(animal)

        else:
            self.dict[animal.species] = [animal]

    def removeAnimal(self, animal):
        if animal.species in self.dict:
            if animal in self.dict[animal.species]:
                self.dict[animal.species].remove(animal)

                return True

    def removeSpecies(self, species):
        if species.upper() in self.dict:
            self.dict.pop(species.upper())

    def getAnimalsBySpecies(self, species):
        species = species.upper()
        collection = []

        if species in self.dict:
            for i in self.dict[species]:
                collection.append(i.toString())

        return "\n".join(collection)

    def doesAnimalExist(self, animal):
        return animal.species in self.dict and animal in self.dict[animal.species]

myShelter = AnimalShelter()

Tiger = Animal("Cat", 200, 20, "Moe")

Leopard = Animal("Cat", 120, 40, "Leopard Man")

Panda = Animal("Bear", 180, 40, "Winnie The Bear")

temp = [Tiger, Panda, Leopard]

for x in temp:
    myShelter.addAnimal(x)

print(myShelter.getAnimalsBySpecies("Cat"))

print(myShelter.doesAnimalExist(Tiger))


for x in "h00":
    print(x[0])
    print(None)
print("out of for loop")