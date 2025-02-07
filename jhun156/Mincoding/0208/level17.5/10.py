arr = [
    [3,1,9],
    [7,2,1],
    [1,0,8],
]

lst = [[i for i in map(int,input().split())] for _ in range(3)]
ans = 0

def isExist(y,x):
    if lst[y][x] == 1:
        if 3 <= arr[y][x] <= 5:
            return 1
    return 0

for i in range(3):
    for j in range(3):
        ret = isExist(i,j)
        ans += ret

if ans == 0:
    print("미발견")
else:
    print("발견")