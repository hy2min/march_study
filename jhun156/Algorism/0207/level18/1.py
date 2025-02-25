record = [
    [65000,35,42,70],
    [70,35,65000,1300],
    [65000,30000,38,42],
]

bucket = [0] * 65535
for i in range(3):
    for j in range(4):
        bucket[record[i][j]] += 1
tmp = max(bucket)
for i in range(65535):
    if bucket[i] == tmp:
        print(i)
