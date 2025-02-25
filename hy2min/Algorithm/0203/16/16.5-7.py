arr = [[0] * 4 for _ in range(7)]

start = 1
for i in range(7):
    for j in range(4):
        arr[i][j] = start
        start += 1
        
lines = list(map(int, input().split()))
for line in lines:
    for i in range(4):
        arr[line][i] = 0

for i in arr:
    for j in i:
        print(j, end=" ")
    print()