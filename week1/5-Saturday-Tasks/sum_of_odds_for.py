n = input("Enter number: ")
n = int(n)

counter = 1
odds = []
sum_of_odds = 0

while counter <= n:
    if not counter % 2 == 0:
        odds += [counter]
    counter +=1

for odd in odds:
    sum_of_odds += odd

print("Sum of odds is %s" % sum_of_odds)
