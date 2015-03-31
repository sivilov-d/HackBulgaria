def divisors(n):
    div = []
    for i in range (1, n):
        if n % i == 0:
            div += [i]
    return div



n = input("Enter nu number: ")
n = int(n)

print(divisors(n))

