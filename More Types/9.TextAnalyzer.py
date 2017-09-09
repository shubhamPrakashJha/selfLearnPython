def char_count(text,char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count


filename = input("enter a filename:")
with open(filename) as f:
    text = f.read()

for char in "Labcdefghijklmnopqrstuvwxyz":
    perc = 100*char_count(text,char)/len(text)
    print("{0} = {1}({2}%)".format(char,char_count(text,char),round(perc,2)))