from random import randint

sides = input("Enter number of sides: ")
repeat = 0
dice_sum = 0

while repeat <=2:
    roll = randint(1, int(sides))
    print("The dice rolled: %s" % roll)
    repeat +=1
    dice_sum += roll

print("Sum is %s" % dice_sum)


