arr = [
    [3,4,1,6],
    [3,5,3,6],
    [0,0,0,0],
    [5,4,6,0],
]

rep = [i for i in map(int,input().split())]

for i in range(4):
    arr[2][i] = rep[i]

MAX, MIN = 0,100
max_x,max_y,min_x,min_y = 0,0,0,0

for i in range(4):
    for j in range(4):
        if arr[i][j] > MAX:
            MAX = arr[i][j]
            max_x, max_y = j, i
        if arr[i][j] < MIN:
            MIN = arr[i][j]
            min_x, min_y = j, i

print(f"MAX={MAX}({max_y},{max_x})")
print(f"MIN={MIN}({min_y},{min_x})")