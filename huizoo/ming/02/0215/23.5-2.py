arr = [[0]*4 for _ in range(3)]
for _ in range(3):
    y, x = map(int, input().split())
    arr[y][x] = '#'
danger = 0
for row in arr:
    if row.count('#') > 1:
        danger = 1
for row in zip(*arr):
    if row.count('#') > 1:
        danger = 1
if danger:
    print('위험')
else:
    print('안전')