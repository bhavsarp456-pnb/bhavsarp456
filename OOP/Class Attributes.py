class User:
    nationality = "Indian"
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

Abhilash = User("Jack","Sparroww",35)
user2 = User("Tonny","Stark",40)

print(Abhilash.nationality)
print(user2.nationality)