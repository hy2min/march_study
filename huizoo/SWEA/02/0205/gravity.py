T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    input_arr = list(map(int, input().split()))
    M = max(input_arr)
    arr = [[0]*N for _ in range(M)]
    for i in range(M) : 
        for j in range(N) : 
            if input_arr[j] :
                arr[-i-1][j] = 1
                input_arr[j] -= 1
 
    drop_list = []
    for i in range(M) :
        for j in range(N) : 
            if arr[i][j] :
                drop_list.append(arr[i][j:].count(0))
 
    print(f'#{test_case} {max(drop_list)}')
