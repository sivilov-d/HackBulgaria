n = input("Enter number: ")
n = int(n)
div_sum = 0

for i in range(1, n):
    if n % i == 0:
        #print(i)
        div_sum += i

if div_sum == n:
    print("Number is perfect")
else:
    print("Number is not perfect")
