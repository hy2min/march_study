N = int(input())
arr = [[0] * 3 for _ in range(3)]
for _ in range(N):
    a,b,c = input().split()
    y = int(a)
    x = int(b)
    plant = list(map(int,c))
    arr[y][x] = plant

M = int(input())
lst = list(map(int,input().split()))
ans = 0

def storm(y,x):

    global arr
    cnt = 0
    while cnt < M:
        if arr[y][x][-1] > lst[cnt]:
            arr[y][x][-1] -= lst[cnt]
            cnt += 1
        else:
            arr[y][x].pop()
            cnt += 1

        if len(arr[y][x]) == 0:
            return 0

    return len(arr[y][x])

for i in range(3):
    for j in range(3):
        if arr[i][j] != 0:
            ans += storm(i,j)

print(ans)