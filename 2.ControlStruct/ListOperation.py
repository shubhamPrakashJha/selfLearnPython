nums = [1,2,3]
print(nums)
print(nums+[3,4,5])
print(nums*3)

words = ["sapm", "egg", "sapm", "sausage"]
print("sapm" in words)
print("not" in words)
print(not "not" in words)
print("not" not in words)

nums.append(4)
print(nums)
print(len(nums))

sentence = ["python", "fun"]
sentence.insert(1,"is")
print(sentence)
print(sentence.index("python"))