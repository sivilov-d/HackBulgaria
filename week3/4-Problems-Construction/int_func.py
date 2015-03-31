n = int(input("Enter number 'n': "))


def to_single(n):
    single_list = []    
    for number in str(n):
        single_list += [int(number)]
        
    return single_list
    


def reverse_int(n):
    d = 0
    for i in range(0, len(str(n))):
        last = n % 10
        d = d*10 + last
        n = n // 10    

    return d


def sum_int(n):
    sum_int = 0
    d = to_single(n)
    for number in d:
        sum_int += number
        
    return sum_int
    

def mult_int(n):
    d = to_single(n)
    mult = 1
    for number in d:
        mult *= number

    return mult



print("Reverse number is %s" % reverse_int(n))
print("Sum of all digits of 'n' is %s" % sum_int(n))
print("Multiplication of all digits in 'n' is %s" % mult_int(n))


