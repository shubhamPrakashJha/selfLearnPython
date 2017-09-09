myfile = open("filename.txt","w")
myfile.write("this has been written 1st time to the file")
myfile.close()

# myfile = open("filename.txt", "r")
# print(myfile.read())
# myfile.close()

msg = "this has been written 2nd time to the file"
myfile = open("filename.txt","w")
count = myfile.write(msg)
myfile.close()

myfile = open("filename.txt", "r")
print(myfile.read())
print(count)
myfile.close()
