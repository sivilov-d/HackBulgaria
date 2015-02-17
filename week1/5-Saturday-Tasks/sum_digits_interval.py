a = input("Enter a: ")
b = input("Enter b: ")

a = int(a)
b = int(b)

sum = 0
counter = int(a)


while a <= b:
    sum = 0
    n = a
    while True:
        last = n % 10
        sum += last
        n = n // 10
        if n < 1:
            print("Sum of digits of %s is %s" % (a,sum))
            break

    a += 1
