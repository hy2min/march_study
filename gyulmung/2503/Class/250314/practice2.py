import sys
sys.stdin = open('input.txt','r')


from collections import deque

N = int(input()) # 예약 팀
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1], x[0]))
print(arr)
q = deque()
q.append((arr[0][0], arr[0][1], 1))
Max = -1e8
while q:
    st, ed, cnt = q.popleft()
    if Max < cnt:
        Max = cnt
    for y, x in arr:
        if y >= ed:
            q.append((y, x, cnt+1))
print(Max)

# 강사님 코드
arr = []
n = int(input())
for _ in range(n):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (x[1], x[0]))

Max, end_time = 0, 0
for start, end in arr:
    if start >= end_time:
        Max += 1
        end_time = end

print(Max)
