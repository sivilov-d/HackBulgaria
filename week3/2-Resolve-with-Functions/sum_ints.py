def divisors(n):
    div = []
    for i in range (1, n):
        if n % i == 0:
            div += [i]
    return div


def sum_ints(numbers):
    sum_div = 0
    a = divisors(numbers)
    for i in a:
        sum_div += i
    return sum_div

n = input("Enter nu number: ")
n = int(n)

print(divisors(n))
print(sum_ints(n))
