class Dog:
    def __init__(self,name, breed):
        self.name = name
        self.breed = breed
        
    def __repr__(self):
        return f"Name: {self.name}\nBreed: {self.breed}"

my_pet = Dog("Maxxu","Beagle")

print(my_pet)
#Without the __repr__method
#print(my_pet)
#it will show a memory location at outpu terminal