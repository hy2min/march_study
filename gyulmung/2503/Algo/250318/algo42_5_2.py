import sys
sys.stdin = open('input.txt','r')

import copy

arr = [list(input()) for _ in range(4)]
n = int(input()) # 폭탄 개수

Min = 1e8
lat = []
path = []
path_ret = []
directy = [0, 0, 1, -1]
directx = [1, -1, 0, 0]

# 폭탄 투하하기
def bomb(lev,lst):
    global arr, Min, path_ret
    if lev == n:
        death = 0
        for i in range(4):
            for j in range(4):
                if arr[i][j] != '_':
                    death += 1
        if Min > death:
            Min = death
            path_ret = copy.deepcopy(path)
        return


    for i in range(4):
        for j in range(4):
            if arr[i][j] != '_':
                y, x = i, j
                path.append((y, x)) # 폭탄 투하 위치 확인
                y, x = path[-1][0], path[-1][1]
                lst = copy.deepcopy(arr)
                for k in range(4):
                    dy = directy[k] + y
                    dx = directx[k] + x
                    if dy < 0 or dx < 0 or dy >= 4 or dx >= 4: continue
                    arr[y][x] = '_'
                    arr[dy][dx] = '_'
                bomb(lev+1, lst)
                arr = lst
                path.pop()


bomb(0, lat)
# print(path_ret)
ret = []
for i, j in path_ret:
    ret.append(arr[i][j])
ret.sort()
print(*ret)
