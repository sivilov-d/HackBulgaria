from random import randint

n = int(input("Enter number: "))
start = int(input("Enter number for start: "))
end = int(input("Enter number for end: "))

def random_numbers(n, start, end):
    number_list = []
    
    for i in range(0, n):
        number = randint(start, end)
        number_list += [number]
        
    return number_list

print(random_numbers(n, start, end))
        
