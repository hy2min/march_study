import sys
sys.stdin=open('input.txt','r')
from collections import deque
# def Find(level, Sum):
#     global count
#     visited2 = visited1
#     if 10 <= Sum <= 20:
#         count += 1
#     if level == len(num):
#         return
#     for i in range(len(num)):
#         if visited2[i] != 1:
#             visited2[i] = 1
#             Find(level+1, Sum + num[i])
#
#
#
# visited1 = [0]*len(num)
# visited2 = []
# count = 0
# for i in range(len(num)):
#     visited1[i] =1
#     Find(i+1, num[i])
# print(count)

def Find(level, Sum):
    global path, combi, cnt
    if 10 <= Sum <= 20:
        if combi in path:
            pass
        else:
            path.append(combi)
            cnt += 1
    if level == len(num):
        return
    for i in range(2): # O(0) 아니면 X(1)
        if i:
            combi += str(num[level])
            Find(level+1, Sum+num[level])
            combi = combi[:-1]
        else:
            Find(level+1, Sum)


path = []
combi = ''
cnt = 0
num = list(map(int, input().split()))
Find(0,0)
print(cnt)