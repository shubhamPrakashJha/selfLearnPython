num_set = {1,2,3,4,5,6}
add_set = {4,5,6,7,8,9}
word_set = set(["spam","eggs","sausage"])

print(3 in num_set)
print("sausage" not in word_set)
#
print(num_set | add_set)
print(num_set & add_set)
print(num_set - add_set)
print(add_set - num_set)
print(num_set ^ add_set)

num_set.add(-5)
print(num_set)
num_set.remove(5)
print(num_set)