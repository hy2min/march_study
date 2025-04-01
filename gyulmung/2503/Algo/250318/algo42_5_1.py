import sys
sys.stdin = open('input.txt','r')

import copy
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
lat = []
Max = -1e8

def rotate(y, x):
    global arr
    for i in range(x):
        a = arr[y][n-1]
        for j in range(n-1, 0, -1):
            arr[y][j] = arr[y][j-1]
        arr[y][0] = a

def dfs(lev):
    global arr, lat, Max
    if lev == n:
        # 위에서 아래의 합의 곱 구하기
        Sum = []
        ret = 1
        for i in range(n):
            sum_l = 0
            for j in range(n):
                sum_l += arr[j][i]
            Sum.append(sum_l)

        for i in Sum:
            ret *= i
        Max = max(Max, ret)
        return

    lat = copy.deepcopy(arr)
    for i in range(n):
        rotate(lev, i)
        dfs(lev+1)
        arr = lat

dfs(0)
print(f'{Max}점')
