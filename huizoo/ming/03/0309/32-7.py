n = int(input())
arr = [[[] for _ in range(3)] for _ in range(3)]

for _ in range(n):
    y, x, num = map(int, input().split())
    lst = list(str(num))
    for i in range(len(lst)):
        lst[i] = int(lst[i])
    arr[y][x] = lst

m = int(input())
winds = list(map(int, input().split()))

for wind in winds:
    for i in range(3):
        for j in range(3):
            if arr[i][j]:
                arr[i][j][-1] -= wind
                if arr[i][j][-1] <=0:
                    arr[i][j].pop()

cnt = 0
for i in range(3):
    for j in range(3):
        cnt += len(arr[i][j])

print(cnt)