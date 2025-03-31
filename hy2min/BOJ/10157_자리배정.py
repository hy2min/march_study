c, r = map(int, input().split())
k = int(input())

if c*r < k: # 배정 불가능한 경우
    print(0)
else:
    di, dj = [1,0,-1,0],[0,1,0,-1]
    arr = [[1]*(c+2)] + [[1]+[0]*c+[1] for _ in range(r)] + [[1]*(c+2)]

    ci, cj, dr = 1,1,0
    for n in range(1,k):
        arr[ci][cj] = n
        ni, nj = ci + di[dr], cj + dj[dr]
        if arr[ni][nj] == 0:
            ci, cj = ni, nj
        else:
            dr = (dr+1) % 4
            ci, cj = ci + di[dr], cj + dj[dr]
    print(f'{cj} {ci}')