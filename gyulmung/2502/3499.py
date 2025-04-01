import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for test in range(1, T+1):
    N = int(input())
    arr = list(map(str, input().split()))
    long_arr = len(arr)
    arr_f = []
    arr_b = []
    result = []
    if long_arr % 2 == 0:
        arr_f = arr[:long_arr//2]
        arr_b = arr[long_arr //2:]
        for i in range(long_arr // 2):
            result.append(arr_f[i])
            result.append(arr_b[i])
    else:
        arr_f = arr[:long_arr // 2 + 1]
        arr_b =arr[long_arr // 2 + 1:]
        for i in range(long_arr // 2):
            result.append(arr_f[i])
            result.append(arr_b[i])
        result.append(arr_f[long_arr//2])


    print(f'#{test}', *result)