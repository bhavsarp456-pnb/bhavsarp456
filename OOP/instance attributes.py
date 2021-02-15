class User:
    def __init__(self,first,last,age, city):
        self.first_name = first
        self.last_name = last
        self.age = age
        self.city = city
    
user1 = User("Jack","Shephard",30,"Canada")
user2 = User("Maxxu","MyPet",30,"Ahmedabad")
print(user1.first_name,user2.first_name)
print(user1.last_name,user2.last_name)
print(user1.age,user2.age)
print(user1.city,user2.city)

