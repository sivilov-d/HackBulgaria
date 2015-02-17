n = input("Enter number: ")
n = int(n)
while True:
    last = n % 10
    print(last)
    n = n // 10
    if n < 1:
        break
