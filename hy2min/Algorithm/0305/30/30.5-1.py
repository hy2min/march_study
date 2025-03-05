from collections import deque

clock = deque([12,9,3,6])
k = int(input())
if k % 360 == 0:
    print(*clock)
elif k % 360 == 90:

elif k % 360 == 180:

elif k % 360 == 270:


