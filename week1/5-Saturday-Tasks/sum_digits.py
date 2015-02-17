n = input("Enter number: ")
n = int(n)
sum = 0
while True:
    last = n % 10    
    sum += last
    n = n // 10
    if n < 1:
        break

print(sum)
