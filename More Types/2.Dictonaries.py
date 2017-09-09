ages = {"dave":24,"mary":42,"john":58}
rgb = {
    "red":[255,0,0],
    "green":[0,255,0],
    "blue":[0,0,255]}
squares = {1:1,2:4,3:"error",4:16}

print(ages["dave"])
print(rgb["red"])
print(rgb["red"][0])

squares[8] = 64
# squares[3] = 9
print(squares)

print(2 in squares)
print("error" in squares)
print(5 not in squares)

print(squares.get("orange"))
print(squares.get(5))
print(squares.get(5,"not in dictionary"))