n = input("Enter number: ")
n = int(n)

digits = []
rev_num = 0

while True:
    last = n % 10
    rev_num = rev_num *10 + last
    n = n // 10
    if n  == 0:
        break

print(rev_num)
