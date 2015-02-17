a = input("Enter number: ")

a = int(a)
rev_number = 0
original = a

while a != 0:
    last = a % 10
    rev_number = rev_number * 10 + last
    a =  a // 10

print(rev_number)

if rev_number - original == 0:
    print("The number is polyndrom")
else:
    print("That number is not polyndrom")


