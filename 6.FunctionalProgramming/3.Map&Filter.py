def add_five(arg):
    return arg+5

arr = [10,20,30,40,50]
result = list(map(add_five,arr))
result2 = list(map(lambda x: x+10,arr))
res = list(filter(lambda x:x%4==0,arr))
print(arr)
print(result)
print(result2)
print(res)
print(arr)