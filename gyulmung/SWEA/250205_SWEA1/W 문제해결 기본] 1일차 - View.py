import sys
sys.stdin = open('input.txt', 'r')

T = 10
for test in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))
    Total_Min = 0
    for i in range(2, N-2):
        L = max(arr[i-1], arr[i-2])
        R = max(arr[i+1], arr[i+2])
        Max = max(L, R)
        if Max < arr[i]:
            Total_Min += arr[i] - Max
    print(f'#{test} {Total_Min}')

for test in range(1, 11):
    N = int(input())
    arr = list(map(int, input().split()))

    Total_cnt = 0

    for i in range(2, N-2):
        Min = 1e8
        for j in range(-2, 3):
            if arr[i] < arr[i+j]:
                Min = 0
                break
            elif arr[i] > arr[i+j]:
                Min = min(Min, arr[i] - arr[i+j])
        Total_cnt += Min
    print(f'#{test} {Total_cnt}')