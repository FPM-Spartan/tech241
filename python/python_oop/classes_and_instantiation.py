# Classes and Instantiation

# creating a class - this is like a template
class Dog:

    animal_kind = "canine" # class variable

    def bark(self): # Class function = methods
        return "woof"

# print(Dog.animal_kind)
# print(Dog.bark(Dog))

# Instantiation of a class

fido = Dog() # Brackets mean this is an object and not a variable
lassie = Dog()

print(type(fido)) # '__main__.Dog'
print(fido.animal_kind) # canine
print(lassie.animal_kind)
print(fido.bark()) # woof
print(lassie.bark())

fido.animal_kind = "Big Dog" # you can overwrite class attributes per instantiation.
print(fido.animal_kind) # Big Dog
print(lassie.animal_kind) # canine

# BE CAREFUL OF CLASS VARIABLES

Dog.animal_kind = "Dolphin"
print(fido.animal_kind) # big dog took precedent over this
print(lassie.animal_kind) # Dolphin