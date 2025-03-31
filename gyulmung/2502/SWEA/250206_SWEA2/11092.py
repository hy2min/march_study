import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test in range(1,T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    Max, Min, Max_in, Min_in = 0, 0, -1e8, 1e8
    Min = min(arr)
    Max = max(arr)
    for i in range(len(arr)):
        if arr[i] == Min:
            Min_in = min(Min_in, i)
        elif arr[i] == Max:
            Max_in = max(Max_in, i)
    result = 0
    if Max_in > Min_in:
        result = Max_in - Min_in
    elif Max_in < Min_in:
        result = Min_in - Max_in

    print(f'#{test} {result}')