#Inheritance

#Base Class
class User:
    #constructor
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def login(self):
        return f"{self.name} has loged in"
#child class Admin inherits from User class
class Admin(User):
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
    def delete_user(self):
        return f"You have deleted a user"
piyush = User("Piyush", "bhavsarp456@gmail.com")
paresh = Admin("Paresh", "bparesh13@gmail.com",12354)
print(piyush.name)
print(paresh.email)
print(paresh.name,paresh.email,paresh.password)
print(piyush.login())
print(paresh.login())
print(paresh.delete_user())