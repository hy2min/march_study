n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def abc():
    d = [(0, 1), (0, -1), (1, 0), (-1, 0), (0, 0)]
    yx = dict()
    for i in range(n):
        for j in range(n):
            yx[arr[i][j]] = (i, j)
    remain = n * n
    for i in range(1, remain+1):
        if remain == 0:
            print(f'{i-1}초')
            return
        y, x = yx[i]
        if arr[y][x]:
            arr[y][x] = 0
            remain -= 1
            for dy, dx in d:
                ny, nx = y+dy, x+dx
                if ny<0 or nx<0 or ny>=n or nx>=n: continue
                if arr[ny][nx]:
                    remain -= 1
                    arr[ny][nx] = 0
    print(f'{n*n}초')

abc()