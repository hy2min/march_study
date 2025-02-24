arr = [list(map(int, input().split())) for _ in range(3)]
dat = [0]*10
for i in range(3):
    for j in range(3):
        dat[arr[i][j]] += 1
for i in range(1, 10):
    if dat[i] == 0:
        print(i, end = ' ')