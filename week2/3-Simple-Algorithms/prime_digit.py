n = input("Enter nuber: ")
n = int(n)

numbers = []

while n !=0:
    last = n % 10
    numbers += [last]
    n = n // 10


#print(numbers)
prime = 0
    
for number in numbers:
    if number in [2, 3, 5, 7]:
        prime = 1
        break
    

if prime == 1:
    print("Yes")
else:
    print("No")
