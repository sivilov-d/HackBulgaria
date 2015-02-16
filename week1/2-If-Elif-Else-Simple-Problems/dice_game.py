from random import randint

sides = input("Enter number of sides: ")

pl_1 = input("Enter the name of Player 1: ")
pl_2 = input("Enter the name of Player 2: ")


dice_1 = randint(1, int(sides))
dice_2 = randint(1, int(sides))

print (pl_1 + " rolled: " + str(dice_1))
print (pl_2 + " rolled: " + str(dice_2))

if dice_1 > dice_2:
    print("Winner is: " + pl_1)
elif dice_1 < dice_2:
    print("Winer is: " + pl_2)
else:
    print("Tie")
    
