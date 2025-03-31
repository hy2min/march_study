import sys
sys.stdin = open('input.txt', 'r')

from collections import deque

N = int(input())
hour = N // 90
arr = [12, 9, 3, 6]
trans = deque()
trans.append(arr)

for i  in range(hour):
    a, b, c, d = trans.popleft()
    trans.append((b, d, a, c))

a, b, c, d = trans.popleft()
print(a, b, c, d)