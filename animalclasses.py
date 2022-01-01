# DEFINING CLASSES

from random import randrange as rand
class Animal:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.id = rand(0, 999)

    def speak():
        pass
    
    def print_data(self):
        return "{}, id {}, is owned by {}".format(self.name, self.id, self.owner)

    def setName(self, newName):
        self.name = newName
    
    def getName(self):
        return self.name

    def setOwner(self, newOwner):
        self.owner = newOwner

    def getOwner(self):
        return self.owner

class Dog(Animal):
    def __init__(self, name, owner, size, gender, color, breed):
        super().__init__(name, owner)
        self.breed = breed
        self.gender = gender
        self.color = color
        self.size = size
        if breed == "m":
            self.pronoun = "his"
        else:
            self.pronoun = "her"

    def speak(self):
        return "'Bark!'"

    def print_data(self):
        return "{} is a {}, {}, {} and {} owner is {}," \
            " also {} says {}".format(self.name, self.size, \
            self.color, self.breed, self.pronoun, self.owner, \
            self.name, self.speak())
