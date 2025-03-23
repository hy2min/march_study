import sys

def Chess(y, x):
    cnt1 = 64
    cnt2 = 64
    for i in range(8):
        for j in range(8):
            if arr[y+i][j+x] == chess1[i][j]:
                cnt1 -= 1
            if arr[y+i][j+x] == chess2[i][j]:
                cnt2 -= 1
    return min(cnt1, cnt2)

N, M = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().rstrip()) for _ in range(N)]
chess1 = [
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
]
chess2 = [
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
    ['B','W','B','W','B','W','B','W'],
    ['W','B','W','B','W','B','W','B'],
]
Min = 100
for i in range(N-7):
    for j in range(M-7):
        if i == 0 and j == 5:
            degub = 1
        ret = Chess(i, j)
        Min = min(Min, ret)
print(Min)