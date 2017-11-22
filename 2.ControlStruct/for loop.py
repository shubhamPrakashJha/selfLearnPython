words = ["sapm", "egg", "sapm", "sausage"]

count = 0

while count < len(words):
    word = words[count]
    print(word+"!")
    count += 1

print("---------------------------------")

for items in words:
    print(items+"@")

print("---------------------------------")

for i in range(4):
    print("hello")