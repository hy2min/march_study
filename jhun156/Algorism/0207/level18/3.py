arr =[
    [1,3,3,5,1],
    [3,6,2,4,2],
    [1,9,2,6,5],
]
N = int(input())

DAT = [0] * 16
for i in range(3):
    for j in range(5):
        DAT[arr[i][j]] += 1

for i in range(1,16):
    if DAT[i] == N:
        print(i, end = ' ')