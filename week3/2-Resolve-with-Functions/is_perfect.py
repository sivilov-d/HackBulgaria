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
        print("Number is perfect")
    else:
        print("Number is not perfect")


n = input("Enter number: ")
n = int(n)

is_perf = is_perfect(n)
print(divisors(n))
print(sum_ints(n))
print(is_perf)
