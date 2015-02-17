n = input("Enter number: ")

counter = 1
sum_ = 0

while counter <= int(n):
    if counter % 2 ==0:
        sum_ += counter
    
    counter +=1    
    
print(sum_)

