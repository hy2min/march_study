import sys
sys.stdin = open('input.txt','r')

from collections import deque
n = int(input())
medal = []
score = []
for i in range(n):
    y, x = input().split()
    score.append((y, x, i))
# print(score)

for i in range(1, n + 1):
    medal = score[0:i]
    medal.sort(key=lambda x:(-int(x[1]),-x[2]))
    # print(medal)
    for i in range(len(medal)):
        if i > 2:
            break
        print(medal[i][0], end = " ")
    print()
