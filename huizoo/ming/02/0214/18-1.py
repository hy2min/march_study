arr = [
    [65000, 35, 42, 70],
    [70, 35, 65000, 1300],
    [65000, 30000, 38, 42],
]
dat = [0]*65536

for i in range(3):
    for j in range(4):
        dat[arr[i][j]] += 1
print(dat.index(max(dat)))