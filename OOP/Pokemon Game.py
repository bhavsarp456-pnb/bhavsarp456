#Pokemon Game

class Pokemon:
    def __init__(self, name, type, **attacks):
        self.name = name
        self.type = type
        self.attacks = attacks
        self._health = 100
    #Getter method for private attribute _health
    def get_health(self):
        return self._health
    def attack(self, attack_name):
        #will return a dictionary. ex {"slash":10}
        return {attack: hitpoints for attack, hitpoints in self.attacks.items() if attack == attack_name}

    def damage(self, attack):
        attack_name = list(attack.keys())[0]
        attack_hitponts = list(attack.values())[0]
        self._health -= attack_hitponts
        print(f"{self.name} got hit by {attack_name} and took a damage of {attack_hitponts}%")

Pikachu = Pokemon("Pikachu", "Electric", slash=10, thunderbolt=25, irontail= 25, electrobolt= 50)
Charlizard = Pokemon("Charlizard", "Fire", slash=12, flamethrower=28, cosmiktoss=60, fireball=40)

print(Charlizard.get_health())
Pikachu.damage(Charlizard.attack("cosmiktoss"))

print(Pikachu.get_health())