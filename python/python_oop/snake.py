# showcasing encapsulation

from reptile import Reptile
# imported Reptile

class Snake(Reptile):
    def __init__(self):
        super().__init__()
        self.forked_tongue = True
        self.cold_blooded = True # This is already in Reptile,but we can redo it here.
        self.venom = None # not all snakes are venomous
        self.limbs = False
        self.Tetrapod = False # We are overwriting this Reptile class for snakes since snakes do not have four legs

    def use_tongue_to_smell(self):
        print("Do I say it smells nice or tastes nice...?")

sidney = Snake()
sidney.breathe() # Animal method
sidney.seek_heat() # Reptile method
sidney.use_tongue_to_smell() # Snake method

# Encapsulation is also really good for protecting important variables/objects
"""
Types of modifiers in Python:

1. Public - anyone, anywhere can use it
2. Private - accessible only within the class itself
3. Protected - accessible within the class and its subclasses

"""