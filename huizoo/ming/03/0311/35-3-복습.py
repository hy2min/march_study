def abc(x, l):
    small = x
    left = 2*x+1
    right = 2*x+2

    if left < l and arr2[small][0] > arr2[left][0]:
        small = left
    if right < l and arr2[small][0] > arr2[right][0]:
        small = right
    if small != x:
        arr2[small], arr2[x] = arr2[x], arr2[small]
        abc(small, l)

def bbq(lst, remains):
    while lst:
        num, y, x = lst.pop()
        if not arr[y][x]: continue
        for dy, dx in d:
            ny, nx = y+dy, x+dx
            if ny<0 or nx<0 or ny>=n or nx>=n: continue
            if not arr[ny][nx]: continue
            arr[ny][nx] = 0
            remains -= 1
            if remains == 0:
                return num


n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [(-1, 0), (1, 0), (0, 0), (0, 1), (0, -1)]
arr2 = []
remains = n**2
for i in range(n):
    for j in range(n):
        arr2.append((arr[i][j], i, j))
length = len(arr2)

for i in range(length//2-1, -1, -1):
    abc(i, length)

for i in range(length-1, 0, -1):
    arr2[0], arr2[i] = arr2[i], arr2[0]
    abc(0, i)

print(f'{bbq(arr2, remains)}초')