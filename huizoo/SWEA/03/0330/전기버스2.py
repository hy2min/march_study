import sys, heapq
sys.stdin = open("input.txt", "r")

def abc():
    now = cnt = 0
    drive = arr[0]
    while 1:
        Max = 0
        cnt += 1
        for i in range(now + 1, now + drive + 1):
            if Max < i + arr[i]:
                Max = i + arr[i]
                if Max >= n:
                    return cnt
                now = i
                drive = arr[i]

T = int(input())
for tc in range(1, T+1):
    n, *arr = map(int, input().split())
    n -= 1
    print(f'#{tc} {abc()}')