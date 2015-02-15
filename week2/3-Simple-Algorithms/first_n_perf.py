n = input("Enter number: ")
n = int(n)

counter = 1
perf_num = 0

while perf_num < n:
    
    div_sum = 0  
    for i in range (1, counter):        
        if counter % i == 0:            
            div_sum +=i
                        
    if div_sum == counter:
        perf_num +=1
        print("Perf_num %s" % counter)

    counter += 1
    
        


    
