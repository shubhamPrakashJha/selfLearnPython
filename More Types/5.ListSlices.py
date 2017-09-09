# squares = [0,1,4,9,16,25,36,49,64,81]
squares  = []
for i in range(9):
    squares.append(i*i)
# cubes
cubes = [i**3 for i in range(9)]
#square of even no.
even_square = [i**2 for i in range(9) if i%2==0]

print(squares)
print(squares[2:6])
print(squares[3:8])
print(squares[0:1])
print(squares[:7])
print(squares[7:])
print(squares[::2])
print(squares[2:9:3]) #from 2 till 7
print(squares[2:8:3]) #from 2 till 7
print(squares[1:-1])
print(squares[::-1])
print("--------------")
print(cubes)
print("--------------")
print(even_square)
