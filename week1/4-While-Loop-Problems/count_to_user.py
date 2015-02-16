n = input("Enter number: ")
counter = 1

print ("Counting from 1 to %s" % n)
while counter <= int(n):
    print (counter)
    counter += 1

print()

print ("Counting from %s to 1" % n)
counter = int(n)
while counter >= 1:
    print(counter)
    counter -= 1
