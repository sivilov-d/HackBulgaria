n = input("Enter number: ")
n = int(n)

numbers = []
counter = 0

while n != 0:
    last = n % 10
    numbers += [last]
    n = n // 10

numbers.reverse()
print("List of digits is: %s" % numbers)

n = 0

for number in numbers:
    n = n * 10 + number

print("Number is %s" % n)
