#dog

class Dog(object):
    def __init__(self, name, breed, day):
        self.name = name
        self.breed = breed
        self.day = day
    def bark(self):
        print(f"{self.name} bow, wow  on {self.day}")
    def wag(self):
        print(f"{self.name} whooosh on {self.day}")

puppy1 = Dog("Tommy","Lab","Wednusday")
puppy2 = Dog("Maxxu","Lab","Friday")

puppy1.bark()
puppy2.wag()