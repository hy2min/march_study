import sys
sys.stdin = open('input.txt','r')

import copy
n = int(input())
arr = list(map(int, input().split()))

def Shoot(score, lst):
    global Max, path_ret, x, arr
    for i in range(n):
        if arr[i] != 0:
            break
        if Max < score:
            Max = score
            path_ret = copy.deepcopy(path)

    lst = copy.deepcopy(arr)
    directx = [-1, 1]
    for i in range(n):
        if arr[i] != 0:
            # score += arr[i]
            for j in range(2):
                dx = directx[j] + i
                if dx < 0 or dx >= n:continue
                arr[dx] = 0
                arr[i] = 0
                # x = j
            path.append(i)
            Shoot(score+lst[i], lst)
            # score -= arr[i]
            path.pop()
            arr = lst

Max = -1e8
path = []
path_ret = []
lst = []
Shoot(0, lst)
x = 0
print(Max)
print(path_ret)
