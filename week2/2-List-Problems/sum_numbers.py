n = input("Enter count for numbers: ")
n = int(n)

sum = 0
count = 1
numbers = []

while count <= n:
    number = input("Enter number: ")
    number = int(number)
    numbers += [number]
    count += 1

for i in numbers:
    sum += i

print("Sum is %s" % sum)
