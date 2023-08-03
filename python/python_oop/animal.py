# Animal class

class Animal:

    def __init__(self):# init = when you make your class, all of these are true
        self.alive = True
        self.spine = True
        self.eyes = True
        self.lungs = True

    def breathe(self):
        print("One breath at a time, in and out")

    def eat(self):
        print("Nom Nom Nom")

    def procreate(self):
        print("Time to find a mate")

    def move(self):
        print("Onwards and upwards")

# breathe is abstracted. You don't need to know how breathe works in order to use it.
cat = Animal()
# cat.breathe()