try:
    myfile = open("filename.txt","w")
    myfile.write("this has been written 1st time to the file")
finally:
    myfile.close()

try:
    myfile = open("filename.txt", "r")
    print(myfile.read())
finally:
    myfile.close()
