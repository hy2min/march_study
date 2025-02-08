map1 = [
    [3,5,1],
    [3,8,1],
    [1,1,5],
]

bitarray = [list(map(int, input().split())) for _ in range(2)]

max_total = -float('inf')
coord_y, coord_x = 0, 0

for y in range(2) : 
    for x in range(2) :
        temp_total = 0         
        for i in range(2) : 
            for j in range(2) : 
                if bitarray[i][j] : 
                    temp_total += map1[y+i][x+j] 
        if temp_total > max_total :
            max_total = temp_total
            coord_y, coord_x = y, x

print(f'({coord_y},{coord_x})')