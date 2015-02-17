list_of_digits = []
counter = 0

while True :
    n = int(input("Please enter a digit: "))
    if n < 0 or n > 9:
        print("Only digits please!")
    else:
        list_of_digits += [n]
        counter +=1
    if counter == 3:
        break

number = 0

for digit in list_of_digits:
    number = number * 10 + digit

print(number)
    

