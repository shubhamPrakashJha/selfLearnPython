nums = [4,5,6]
msg1 = "numbers: {0}{1}{2}".format(nums[0],nums[1],nums[2])
msg2 = "numbers: {0}{1}{2}".format(nums[0],nums[1],nums[0])
a = "{x},{y}".format(x=5,y=12)
b = "{x}{y}".format(x=5,y=12)
print(msg1)

print(msg2)
print(a)
print(b)