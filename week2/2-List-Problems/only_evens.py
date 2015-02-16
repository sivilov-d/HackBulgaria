n = input("Enter count for numbers: ")
n = int(n)

start = 1
numbers = []
even_numbers = []
even_sum = 0

while start <= n:
    number = int(input("Enter number: "))
    numbers += [number]
    start +=1

for i in numbers:
    if i % 2 == 0:
        even_sum += 1
        even_numbers += [i]
        
print()
print("Count of evens: %s" % even_sum)
print("Evens are: ")

for i in even_numbers:
    print(i)
