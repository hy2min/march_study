from collections import deque

clock = deque([12, 3, 6, 9])
k = int(input())
rotate = (k % 360) // 90
for i in range(rotate):
    clock.appendleft(clock.pop())

print(clock[0], clock[3], clock[1], clock[2])
