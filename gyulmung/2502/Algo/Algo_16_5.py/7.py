arr=[[0]*4 for _ in range(7)]
point = 1
for i in range(7):
    for j in range(4):
        arr[i][j] = point
        point += 1

A = list(map(int, input().split()))

for i in A:
    for j in range(4):
        arr[i][j] = 0

for i in range(7):
    for j in range(4):
        print(arr[i][j], end = " ")
    print()