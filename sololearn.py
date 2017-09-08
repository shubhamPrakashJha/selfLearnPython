print("hello world")
print(int("2")+int("3"))
#sum = int(input("enter first no."))+int(input("enter seconfd no."))
#print(sum)
foo = "string"
print(foo)
print("----------------------------")
my_boolean = True
print(my_boolean)
print(2==3)
print("hello"=="hello")
print("----------------------------")

# if 10>5:
#     print("10 is greater")
# print("condition ended")
# num = int(input("input a no."))
# if (num >5):
#     print("greater than 5")
#     if (num < 20):
#         print("AND between 5 AND 20")
#     else :
#         print("and greater than 20")
# elif num ==5:
#     print("is equal to 5")
# else:
#     print("less than 5")
#
# print("---------------------------")
#
# if(num > 1 and num <4 and not num == 2:
#     print("number is 3")

print("----------------------------")

i = 0
while i<5:
    i = i+1
    if i == 2:
        print("skipping")
        continue
    if i == 4:
        print("breaking")
        break
    print(i)
print("finished")

print("------------------------------")

words = ["hello","world","!"]
print(words[1])

number = 3
things =["string",0,[1,2,number],4.56]
print(things[0])
print(things[2][2])
print(words*3)
print("string" in things)
print("string" not in things)
print("--------------------------------")

numbers1 = list(range(10))
numbers2 = list(range(2,10))
numbers3 = list(range(2,10,2))
print(numbers1)
print(numbers2)
print(numbers3)
print(range(20)==range(0,20))

print("-------------------------------")
for var in words:
    print(var + "!")
print(list(range(5)))
for i in range(5):
    print(i+1)