arr = [
    [3,4,1,6],
    [3,5,3,6],
    [0,0,0,0],
    [5,4,6,0]
]


arr2 = list(map(int,input().split()))


for i in range(4) :
    arr[2][i] = arr2[i]

max_v = arr[0][0]
min_v = arr[0][0]
max_point = [0,0]
min_point = [0,0]

for i in range(4) :
    for j in range(4) :
        if arr[i][j] > max_v :
            max_v = arr[i][j]
            max_point = [i,j]
        if arr[i][j] < min_v :
            min_v = arr[i][j]
            min_point= [i,j]

print(f"MAX={max_v}({max_point[0]},{max_point[1]})")
print(f"MIN={min_v}({min_point[0]},{min_point[1]})")


