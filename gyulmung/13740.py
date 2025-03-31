import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(str, input())) for _ in range(N)]
    half = len(arr) // 2

    for i in range(N):
        for j in range(N):
            if len(arr[i]) % 2 == 0:
                for k in range(half):
                    if arr[half - i] != arr[half + i + 1]:
                        break
                    print(*arr[i], sep = '')
                    else:
                        for k in range(half):
                            if arr[half - i] != arr[half + i]:
                                break
            print(*arr[i], sep = '')