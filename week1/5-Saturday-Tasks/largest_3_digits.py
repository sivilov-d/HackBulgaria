n = input("Enter number: ")
n = int(n)

digits = []

while n != 0:
    last = n % 10
    digits += [last]
    n = n // 10


digits.sort()
min_num = 0

for digit in digits:
    min_num = min_num*10 + digit

print("Min number that you can have is %s" % min_num)

digits.reverse()
max_number = 0

for digit in digits:
    max_number = max_number*10 + digit

print("Max number that you can have is %s" % max_number)

