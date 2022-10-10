class Animal:
    def __init__(self, species = None, weight = None, age = None, name = None):
        self.species = species.upper() if species else species
        self.weight = float(weight) if weight else weight
        self.age = int(age) if age else age
        self.name = name.upper() if name else name

    def setSpecies(self, species):
        self.species = species.upper()

    def setWeight(self, weight):
        self.weight = float(weight)

    def setAge(self, age):
        self.age = int(age)

    def setName(self, name):
        self.name = name.upper()

    def toString(self):
        return f"Species: {self.species}, Weight: {self.weight}, Age: {self.age}, Name:{self.name}"

Cat = Animal()

