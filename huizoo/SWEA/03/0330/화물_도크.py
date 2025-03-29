import sys
sys.stdin = open("input.txt", "r")


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort(key=lambda x:x[1])
    end = 0
    cnt = 0
    for s, e in arr:
        if end <= s:
            cnt += 1
            end = e

    print(f'#{tc} {cnt}')