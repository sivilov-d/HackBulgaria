n = input("Enter number: ")
n = int(n)

print("Divisors of %s are:" % n)
for i in range(1, n):
    if n % i == 0:
        print(i)
    
