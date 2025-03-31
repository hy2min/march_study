n = int(input())
arr = [[] for _ in range(5)]
for _ in range(n):
    a, b = input().split()
    a, b = ord(a)-64, ord(b)-64
    arr[a].append(b)
    arr[b].append(a)


def search(c, p):
    visited[c] = 1
    for cc in arr[c]:
        if visited[cc]:
            if cc != p:
                return 1
        else:
            ret = search(cc, c)
            if ret:
                return 1
    return 0

visited = [0]*5
for i in range(4):
    if visited[i]: continue
    ret = search(i, 0)
    if ret:
        break

if ret:
    print('발견')
else:
    print('미발견')