class Chicken:
    total_eggs = 0
    
    def __init__(self, name, species, eggs=0):  
        self.name = name
        self.species = species
        self.eggs = eggs
        
    def lay_egg(self):
        self.eggs += 1
        Chicken.total_eggs += 1
        