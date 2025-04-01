import sys
sys.stdin = open('input.txt', 'r')

T = 10
for test in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    for i in range(N):
        Max_box = max(arr)
        Min_box = min(arr)
        for j in range(len(arr)):
            if arr[j] == Max_box:
                arr[j] -= 1
                break
        for j in range(len(arr)):
            if arr[j] == Min_box:
                arr[j] += 1
                break
    result = max(arr) - min(arr)
    print(f'#{test} {result}')