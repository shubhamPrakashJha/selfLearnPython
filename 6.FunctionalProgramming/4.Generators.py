def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1

for i in countdown():
    print(i)

print("-----------------------")

def infinite_four():
    for i in range(4):
        yield 4

for i in infinite_four():
    print(i)

print("-----------------------")

def numbers(x):
    for i in range(x):
        if i%2==0:
            yield i

print(list(numbers(11)))
for i in numbers(11):
    print(i)