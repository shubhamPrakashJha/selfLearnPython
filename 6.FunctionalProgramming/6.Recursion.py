def factorial(x):
    if x == 1:
        return 1
    else:
        return x*factorial(x-1)

print(factorial(int(input("enter the number: "))))

def is_even(x):
    if x == 0:
        return True
    else:
        return is_odd(x-1)

def is_odd(x):
    return not is_even(x)

print(is_even(23))
print(is_odd(1))
print(is_odd(2))