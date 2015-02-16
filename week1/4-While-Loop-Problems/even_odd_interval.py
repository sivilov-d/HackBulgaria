a = input("Enter a: ")
b = input("Enter b: ")

a = int(a)
b = int(b)

while a <= b:
    if a % 2 == 0:
        print ("%s is even" % a)
    else:
        print ("%s is odd" % a)
    a += 1
