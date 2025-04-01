import sys
sys.stdin = open('input.txt', 'r')

import copy
n = int(input())
arr = list(map(int, input().split()))

def Shoot(score, lst):
    global Max, path_ret, arr

    start = True # 과녁에 쏠곳이 있는지 확인
    for i in range(n):
        if arr[i] != 0: # 있다면 재귀 진행
            start = False
            break

    if start: # arr에 화살을 쏠곳이 없으면 max 값 및 좌표 저장 후 리턴
        if Max < score:
            Max = score
            path_ret = copy.deepcopy(path)
        return

    directx = [-1, 1]
    for i in range(n):
        lst = copy.deepcopy(arr)
        if arr[i] != 0:
            for j in range(2): # 화살쏜곳 좌우 불태우기
                dx = directx[j]+i
                if dx < 0 or dx >= n: continue
                arr[dx] = 0
                arr[i] = 0
            path.append(i)
            Shoot(score+lst[i], lst)
            path.pop()
            arr = lst
path = []
path_ret = []
lst = []
Max = 0
Shoot(0, lst)
q = []
while 1:
    if not path_ret:
        break
    q.append(str(arr[path_ret.pop(0)]))
    q.append('+')
q.pop()
q.append('=')
q.append(str(Max))
q="".join(q)
print(q)
