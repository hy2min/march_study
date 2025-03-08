arr = [
    [3,5,4,2,5],
    [3,3,3,2,1],
    [3,2,6,7,8],
    [9,1,1,3,2],
]
size_y, size_x = map(int, input().split())

def total(y, x) : 
    temp_total = 0
    for i in range(size_y) : 
        for j in range(size_x) : 
            temp_total += arr[y+i][x+j]
    return temp_total

max_total = 0
y, x = 0, 0
for i in range(4-size_y+1) : 
    for j in range(5-size_x+1) : 
        current_total = total(i, j)
        if max_total < current_total : 
            max_total = current_total
            y, x = i, j
print(f'({y},{x})')