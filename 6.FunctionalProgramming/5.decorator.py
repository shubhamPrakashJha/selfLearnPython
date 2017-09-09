def decor(func):
    def wrap():
        print("=============")
        func()
        print("=============")
    return wrap #if wrap()

def print_text():
    print("HELLO WORLD")

@decor
def print_name():
    print("hey shubham")


decor(print_text)() #then decor(print_text) coz here wrap is returned not wrap()
print_name()