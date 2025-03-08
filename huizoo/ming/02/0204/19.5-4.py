arr = [[0]*4 for _ in range(4)]
input_arr = [input().split() for _ in range(3)]
for row in input_arr : 
    if row[0] == 'G' :
        arr[int(row[1])] = [1]*4
    elif row[0] == 'S' : 
        for i in range(4) :
            arr[i][int(row[1])] = 1

for row in arr : 
    print(*row)