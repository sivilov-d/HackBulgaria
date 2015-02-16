num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")

print("Select operation:")
print("Type '+' to add, '-' to subtract, '*' to multiply or '/' to devide")


oper = input()

if oper == "+":
    add = int(num_1) + int(num_2)
    print("The result is: " + str(add))

elif oper == "-":
    sub = int(num_1) - int(num_2)
    print("The result is: "+ str(sub))

elif oper == "*":
    multi = int(num_1) * int(num_2)
    print("The result is: " + str(multi))

elif oper == "/":
    div = int(num_1) / int(num_2)
    print ("The result is: " + str(div))

else :
    print("We do not support this operation")




#print (oper)
