n = input("Enter count for numbers: ")
n = int(n)

count = 1
numbers = []

while count <= n:
    number = int(input("Enter number: "))
    numbers += [number]
    count += 1

numbers.sort()
print("Min is %s" % numbers[0])

    
