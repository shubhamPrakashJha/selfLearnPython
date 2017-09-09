#named function
def polynomial(x):
    return x**2+x*5+5
print(polynomial(-4))

#lambda function
#       for single line expression
print((lambda x: x**2+x*5+5)(-4))

double = lambda x: x**2+x*5+5
print(double(-4))