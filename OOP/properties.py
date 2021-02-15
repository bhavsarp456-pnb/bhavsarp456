class Animal:
    def __init__(self, species, name):
        self._species = species
        self.name = name
    
    @property
    def species(self):
        return self._species
    
    @species.setter
    def species(self, new_species_name):
        self._species = new_species_name

beerus = Animal("Tiger", "Berus the distroyer")
print(beerus.species)
beerus.species = "Human"
print(beerus.species)