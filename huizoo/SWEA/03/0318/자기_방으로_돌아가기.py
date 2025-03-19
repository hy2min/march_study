import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    room = [0]*201
    for _ in range(N):
        start, end = map(int, input().split())

        start = (start+1)//2
        end = (end+1)//2

        if start > end:
            start, end = end, start

        for i in range(start, end + 1):
            room[i] += 1

    print(f'#{tc} {max(room)}')

# T = int(input())
# for tc in range(1, T+1):
#     N = int(input())
#     arr = []
#     for _ in range(N):
#         a, b = map(int, input().split())
#         arr.append((min(a, b), max(a, b)))
#
#     arr.sort(key=lambda x:x[0])
#     time = 0
#     cnt = 0
#     student = [0]*N
#     while cnt < N:
#         time += 1
#         ed = -1
#         for i in range(N):
#             if student[i]: continue
#             start, end = arr[i]
#             if start > ed:
#                 cnt += 1
#                 student[i] = 1
#                 ed = end if end % 2 == 0 else end + 1
#
#     print(f'#{tc} {time}')
