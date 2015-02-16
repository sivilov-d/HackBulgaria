count = 0
index_names = ['first', "second", "third"]

while count <= 2:    
    index_names[count] = input("Enter your " + index_names[count] + " name: ")
    count += 1
    
    
print("Your full name is: " + " ".join(index_names))

