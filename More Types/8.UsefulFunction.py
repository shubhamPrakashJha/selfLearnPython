print(":".join(["spam","eggs","ham"]))
print("hello ME".replace("ME","world"))
print("check start".startswith("check"))
print("check end".endswith("end"))
print("making it UPPER case".upper())
print("MAKING IT lower CASE".lower())
print("spam:eggs:ham".split(":"))
print("------math------------")
print(min(1,2,3,4,5,5,6,7,8))
print(max(1,2,3,4,5,5,6,7,8))
print(abs(-23))
print(abs(23))
print(sum([1,2,3,4,5,5,6,7,8]))
print("------if--------------")
nums = [55,44,33,22,11]
if all(i>5 for i in nums):
    print("all greater than 5")
if any(i%2 ==0 for i in nums):
    print("atleast one is even")
for v in enumerate(nums):
    print(v)