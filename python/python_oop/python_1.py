# Showcasing polymorphism

from snake import Snake
class Python(Snake):
    def __init__(self):
        super().__init__()
        self.large = True
        self.two_lungs = True
        self.venom = False

    def digest_large_prey(self):
        print("ok, hand me the stretchy pants")

    def constrict(self):
        print("and...squeeeeeze")

    def climb(self):
        print("up we go")

    def shed_skin(self):
        print("I'm growing out of this now")

    def breathe(self):
        print("I am breathing but I am a Python!")