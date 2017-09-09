def apply_twice(func,arg):
    return func(func(arg))
def add(arg):
    return arg +5

print(apply_twice(add,10))