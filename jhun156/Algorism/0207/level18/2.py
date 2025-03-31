arr = [[i for i in map(int,input().split())] for _ in range(3)]

DAT = [0] * 10

for i in range(3):
    for j in range(3):
        DAT[arr[i][j]] += 1

for i in range(1,10):
    if DAT[i] == 0:
        print(i, end = ' ')