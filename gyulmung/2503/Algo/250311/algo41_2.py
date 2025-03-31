# 나중에 풀것
# DP 동적계획법 배우고 풀기

import sys
sys.stdin = open('input.txt','r')

n = int(input())
arr = list(map(int, input().split()))

def mario(lev, cnt):
    global Max
    if lev >= n:
        if Max < cnt:
            Max = cnt

    for i in range(2):
        if lev+i >= n:
            continue
        cnt += arr[lev + i]
        mario(lev+jump[i], cnt)

jump = [2, 7]
Max = -1e8
mario(-1, 0)
print(Max)