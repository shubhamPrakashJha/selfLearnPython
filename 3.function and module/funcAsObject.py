def multiply(x,y):
    return x*y
mul = multiply
print(mul(2,3))

print("-----------")

def add(x,y):
    return x+y
def do_twice(func,x,y):
    return func(func(x,y),func(x,y))
a = 5
b = 10

print(do_twice(add,a,b))