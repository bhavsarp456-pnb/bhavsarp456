class User:
    total_users = 0

    def __init__(self, first, last):
        self.first = first
        self.last = last
        User.total_users += 1
    
    @classmethod
    def get_total_users(cls):

        return total_users

jack = User("Jack", "Sparrow")
tonny = User("Tonny","Stark")

print(jack.get_total_users())
print(User.get_total_users())