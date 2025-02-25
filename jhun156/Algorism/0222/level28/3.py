# ABC 순서대로 인덱스 번호 부여
# 인접 행렬로 풀이
from collections import deque

a = input()
name = 'ABCDEFGH'
near_matrix = [
    [0,1,1,0,0,0,0,1],
    [0,0,0,0,0,0,0,0],
    [0,0,0,1,1,0,1,0],
    [0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0],
]

index = name.index(a)

ans = -1
for i in range(8):
    if near_matrix[i][index] == 1:
        ans = i
        break

lst = []
for i in range(8):
    if near_matrix[ans][i] == 1 and i != index:
        lst.append(i)

if ans == -1:
    print("없음")
else:
    for i in range(len(lst)):
        print(name[lst[i]],end=' ')