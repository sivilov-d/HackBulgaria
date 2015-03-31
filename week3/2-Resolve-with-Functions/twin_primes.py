n = input("Enter number: ")
n = int(n)

a = n - 2
b = n + 2

d = [n, a, b]

def is_prime(n):
    is_prime = True
    
    for i in range (2, n):
        if n % i == 0:
            is_prime = False
            break

    return is_prime

d_1 = []
for i in d:    
    
    if is_prime(i):
        d_1 =  d_1 + [True]
    else:
        d_1 =  d_1 + [False]


      
if not d_1[0]:
    print("%s in not prime" % n)
elif not False in d_1:
    print (a, b)
else:
    if not d_1[1] and not d_1[2]:
        print("%s is prime but %s and %s are not" % (n, a, b))
    elif not d_1[1]:
        print(n, b)
    else:
        print(n, a)
        
        

print(d_1)
