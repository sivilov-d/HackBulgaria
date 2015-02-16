n = input("Enter number: ")
n = int(n)

count = 1
names = []

while count <= n:
    name = input("Enter a name: ")
    names += [name]
    count += 1

names.sort()

print()
print("Sorted names are: ")
for name in names:
    print(name)

        
