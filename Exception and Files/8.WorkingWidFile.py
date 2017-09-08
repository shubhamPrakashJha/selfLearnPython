try:
    myfile = open("filename.txt","w")
    myfile.write("this has been written 1st time to the file")
finally:
    myfile.close()


with open("filename.txt", "r") as myfile:
    print(myfile.read())
