class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed, age):
        super().__init__("dog", name)
        self.breed =breed
        self.age = age

dexter = Dog("Dexter", "hound", 30)
print(dexter.species)
print(dexter.breed)