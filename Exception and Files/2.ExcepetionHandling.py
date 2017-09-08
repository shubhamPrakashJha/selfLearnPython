try:
    num1 = int(input("1st no:"))
    num2 = int(input("2nd no:"))#not converted to int
    print(num1/num2)
except ZeroDivisionError:
    print("An error occured due to zero divion")
except(ValueError,TypeError):
    print("Error occured")
finally:
    print("this code will run no matter what")