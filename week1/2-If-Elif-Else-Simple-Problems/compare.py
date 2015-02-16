a = input("Ënter a: ")
b = input("Enter b: ")

if a == b:
    print("'a' is equal to 'b'")
else:
    if a > b:
        print("a(%s) is bigger than b(%s)" % (a, b))
    else:
        print("b(%s) is bigger than a(%s)" % (b, a))
