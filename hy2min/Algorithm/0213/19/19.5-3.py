arr = [[0]* 4 for _ in range(4)]
start = 1
for i in range(4):
    for j in range(4):
        arr[i][j] = start
        start += 1
ans = [[0] * 4 for _ in range(4)]
lst = list(map(int, input().split()))
for n in range(len(lst)):
    for i in range(4):
        for j in range(4):
            if arr[i][j] == lst[n]:
                ans[i][j] = n+1

for i in ans:
    for j in i:
        print(j, end=" ")
    print()