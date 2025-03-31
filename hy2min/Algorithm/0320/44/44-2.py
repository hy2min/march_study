height, width = map(int, input().split())
arr = [list(input()) for _ in range(height)]

n = int(input())
pn = [list(input()) for _ in range(n)]


for i in range(height-n):
    for j in range(width-n):
        for k in range(n):
            if arr[i+k][j:j+n] == pn[k]:
                flag = 1
