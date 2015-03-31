n = int(input("Enter number: "))

def fib(n):
    fib_list = []
    if n == 1:
        fib_list = [1]
    elif n == 2:
        fib_list = [1, 1]
    else:
        fib_list = [1, 1]
        i = 2
        for j in range (0, n - 2):
            next_fib = fib_list[i-1] + fib_list[i-2]
            fib_list += [next_fib]
            i += 1

    return fib_list


fib_num = 0
for number in fib(n):    
    up = len(str(number))  
    fib_num = fib_num*(10**up) + number

print(fib(n))    
print(fib_num)   


