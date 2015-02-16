from random import randint

sides = input("Enter number of sides: ")
roll = randint(1, int(sides))
print("The dice rolled %s" % roll)
