left_margin = input("Enter number for left margin: ")
right_margin = input("Enter number for right margin: ")
test_int = input("Enter number for test: ")

left_margin = int(left_margin)
right_margin = int(right_margin)
test_int = int(test_int)

if test_int == left_margin:
    print("The number is equal to the lower bound of the interval")
elif test_int == right_margin:
    print("The number is equal to the upper bound of the interval")
elif test_int > left_margin and test_int < right_margin:
    print("The number is in the interval")
else:
    if test_int < left_margin:
        print("The number is outside the interval, x < a")
    else:
        print("The number is outside the interval, x > b")
