phrase = input("Type something: ")

vow_count = 0
vowels = "aeiouy"

phrase = phrase.lower()
#print(phrase)

for char in phrase:
    if char in vowels:
        vow_count +=1

print("Total vowels found: %s" % vow_count)
