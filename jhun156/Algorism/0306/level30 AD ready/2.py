# import sys
# sys.stdin = open("input.txt","r")
from copy import deepcopy

a = [list(map(int,input().split())) for _ in range(3)]
t = input()
b = [list(map(int,input().split())) for _ in range(3)]


cnt = 0

while True:
    cnt += 1
    tmp = deepcopy(a)
    for i in range(3):
        for j in range(3):
            a[i][j] = tmp[j][2-i]
    if a == b:
        print(cnt)
        break


