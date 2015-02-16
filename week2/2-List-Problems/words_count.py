word = input("Enter a word: ")
n = input("Enter number: ")
n = int(n)

count = 1
words = []
total_sum = 0

while count <= n:
    new_word = input("Enter new word: ")
    words += [new_word]
    count += 1

for i in words:
    if word == i:
        total_sum += 1
        
print(word + " is found %s times" % total_sum)
