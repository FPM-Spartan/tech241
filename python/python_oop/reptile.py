# showcasing Inheritance

from animal import Animal # Imports a class from another python file.import

class Reptile(Animal): # Adding Animal into the brackets tells python to use it as a template for the new class

    def __init__(self):
        super().__init__() # Initialises the parent/base class - inherit everything from Animal.
        self.cold_blooded = True
        self.tetrapod = None # not all reptiles have four legs
        self.heart_chambers = [3, 4] # reptiles can have 3 or 4 heart chambers
        self.amniotic_eggs = None # not True for all reptiles

    def seek_heat(self):
        print("it's chilly outside, I need a sunbed")

    def hunt(self):
        print("Hunting prey")

    def use_venom(self):
        print("If I have it, may as well use it")

    def attract_mate_through_scent(self):
        print("Time to put on some aftershave")

bulbasaur = Reptile()

# bulbasaur.hunt() # Reptile Method
# bulbasaur.breathe() # Animal Method
