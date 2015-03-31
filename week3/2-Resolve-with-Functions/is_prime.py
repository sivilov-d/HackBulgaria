n = input("Enter number: ")
n = int(n)

def is_prime(n):
    is_prime = True
    
    for i in range (2, n):
        if n % i == 0:
            is_prime = False
            break

    return is_prime


def to_digits(n):
    d = []
    while n > 0:
        last = n % 10
        d = [last] + d
        n = n // 10

    return d


numbers = to_digits(n)
find_prime = False

for number in numbers:    
    if is_prime(number):
        find_prime = True
        break


if find_prime:
    print("Number has prime digit in it")
else:
    print("Number doesn't have prime digit in it")


