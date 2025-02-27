import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input()))
    cnt, Max = 0, -1e8
    for i in range(N):
        if arr[i] == 1:
            cnt += 1
            Max = max(Max, cnt)
        else:
            cnt = 0
    print(f'#{test} {Max}')