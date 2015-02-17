n = input("Enter a number: ")
counter = 1
fact = 1

if int(n) == 0:
    print(1)
else:    
    while counter <= int(n):
        fact = fact * counter
        counter += 1
    print(fact)

