from os import system

from animalclasses import Animal, Dog

_ = system('clear')

animals = []

entry = 0
while entry != 9:
    type = input("Generic Animal (1), or Dog (2): ")
    if type == '1':
        name = input("Animal's name: ")
        owner = input("Owner of animal: ")
        animal = Animal(name, owner)
        animals.append(animal)
        print(animal.print_data())
    else:
        name = input("Animal's dog: ")
        owner = input("Owner of dog: ")
        size = input("Size (s, m, l): ")
        gender = input("Gender (m, f): ")
        color = input("Color: ")
        breed = input("Breed: ")
        animal = Dog(name, owner, size, gender, color, breed)
        animals.append(animal)
    entry = int(input("Next animal (1) or stop (9): "))

for x in animals:
    print(x.print_data())