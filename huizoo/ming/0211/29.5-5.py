arr = [list(map(int, input().split())) for _ in range(4)]

start = [3,4]
end = [0, 0]
for i in range(4):
    for j in range(5):
        if arr[i][j] == 1 : 
            if start[0] > i: 
                start[0] = i
            if end[0] < i:
                end[0] = i
            if start[1] > j:
                start[1] = j
            if end[1] < j:
                end[1] = j

print(f'({start[0]},{start[1]})')
print(f'({end[0]},{end[1]})')