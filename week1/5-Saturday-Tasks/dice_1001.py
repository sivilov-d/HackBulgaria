from random import randint

player_1 = input("Enter name of player 1: ")
player_2 = input("Enter name of palyer 2: ")

pl1_score = 1001
pl2_score = 1001
score = 1001
round_count = 1

while score != 0:
    if round_count % 2 == 0:
        print(player_1 + "'s turn")
        score = pl1_score
        n = 0
    else:
        print(player_2 + "'s turn")
        score = pl2_score
        n = 1
        
    counter = 1
    roll_sum = 0
    while counter <= 5:
        roll = randint(1,6)
        roll_sum += roll
        print("Dice %s rolls %s" % (counter,roll))
        counter += 1
        
    if score > 0:
        score -= roll_sum
    else:
        score += roll_sum
        
    print("Sum of all rolls = %s" % roll_sum)
    print("Current score is %s" % score)
    print()

    if n == 0:
        pl1_score = score
    else:
        pl2_score = score

    round_count += 1

if n == 0:
    print(player_1 + " wins!")
else:
    print(player_2 + " wins!")
