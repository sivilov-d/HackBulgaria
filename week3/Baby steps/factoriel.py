n = input("Enter number: ")
n = int(n)

def fact(n):
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i += 1
    return fact


print(fact(n))
