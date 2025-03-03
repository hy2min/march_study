h, w = map(int, input().split())
lst = [list(input()) for _ in range(h)]

ans = [[-1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if lst[i][j] == 'c':
            ans[i][j] = 0
        for k in range(j+1, w):
            if lst[i][j] == 'c':
                ans[i][k] = k-j

for i in ans:
    print(*i)