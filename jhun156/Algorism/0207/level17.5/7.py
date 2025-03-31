levelTable = [
    [10,20],
    [30,60],
    [100,150],
    [200,300],
]

arr = [i for i in map(int,input().split())]

result = [0] * 4

for i in range(4):
    for j in range(6):
        if levelTable[i][0] <= arr[j] <= levelTable[i][1]:
            result[i] += 1

for i in range(4):
    print(f"lev{i}:{result[i]}")

