a = input("Enter a: ")
b = input("Enter b: ")

max_ = max(int(a),int(b))
min_ = min(int(a),int(b))

if min_ == max_:
    print("Enter different numbers")
else:
    while min_ <= max_:
        print (min_)
        min_ +=1
