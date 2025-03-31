arr = [
    [3,2,5,3],
    [7,6,1,6],
    [4,9,2,7],
]
times = list(map(int,input().split()))

re_arr = list(map(list,zip(*arr)))

rotation = []
for i in range(len(times)):
    row = re_arr[i]
    rotation_needed = times[i]
    rotated_row = row[3-rotation_needed:] + row[:3-rotation_needed]

    rotation.append(rotated_row)

for i in range(len(rotation[0])): 
    for j in range(len(rotation)): 
        print(rotation[j][i], end="")
    print()