n = input("Enter number: ")
n = int(n)

counter = 1
evens = []
sum_of_evens = 0

while counter <= n:
    if counter % 2 == 0:
        evens += [counter]
    counter +=1

for even in evens:
    sum_of_evens += even

print("Sum of evens is %s" % sum_of_evens)
