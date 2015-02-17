n = input("Enter number: ")
n = int(n)

prime = 1

for i in range (2, n):
    if n % i == 0:
        prime = 0
        break

if prime == 1:
    print("Prime number")
else:
    print("Not Prime number")
    
