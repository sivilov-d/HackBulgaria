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


def is_perfect(n):
    if sum_ints(n) == n:
        return True


def first_n_perf(n):
    d = []
    for i in range (2, n+1):
        if sum_ints(i) == i:
            d += [i]
    return d
     
    

    
n = input("Enter number: ")
n = int(n)

print(first_n_perf(n))
