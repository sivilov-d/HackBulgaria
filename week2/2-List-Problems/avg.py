n = input("Enter count for numbers: ")
n = int(n)

count = 1
numbers = []
total_sum = 0

while count <= n:
    number = int(input("Enter new number: "))
    numbers += [number]
    count += 1

for i in numbers:
    total_sum += i

avg = total_sum / len(numbers)    
print("Avg is %s" % avg)
