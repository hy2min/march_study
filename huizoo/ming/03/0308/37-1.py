N = int(input())
arr = [[0]*N for _ in range(N)]
coo = list(map(int, input().split()))
queue = []
for i in range(0, len(coo), 2):
    queue.append((coo[i], coo[i+1]))
    arr[coo[i]][coo[i+1]] = 1

d = [(-1, 0), (0, -1), (0, 1), (1, 0)]
while queue:
    y, x = queue.pop(0)
    for dy, dx in d:
        ny, nx = y+dy, x+dx
        if ny<0 or nx<0 or ny>=N or nx>=N: continue
        if arr[ny][nx]: continue
        arr[ny][nx] = arr[y][x] + 1
        queue.append((ny, nx))

print('\n'.join(''.join(map(str, row)) for row in arr))