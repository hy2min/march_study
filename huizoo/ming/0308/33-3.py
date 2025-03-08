n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * n

def abc(c, p):
    visited[c] = 1
    for i in range(n):
        if arr[c][i]:
            if not visited[i]:
                if abc(i, c):
                    return 1
            elif i != p:
                return 1
    return 0

flag = 0
for i in range(n):
    if not visited[i]:
        if abc(i, -1):
            flag = 1
            break

if flag:
    print('cycle 발견')
else:
    print('미발견')