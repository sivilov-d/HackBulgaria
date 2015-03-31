block = int(input("Enter number of blocks: "))

print("Enter hight for each block: ")


height_list = []
for i in range (1, block + 1):
    
    height = int(input("Block %s, height: " % i))
    height_list += [height]

counter = 1

i = 0
highest = height_list[0]
for height in height_list:
    if i == len(height_list) - 1:
        break
    if height_list[i+1] > highest:
        counter += 1
        highest = height_list[i+1]
    i += 1


print(height_list)
print(counter)

