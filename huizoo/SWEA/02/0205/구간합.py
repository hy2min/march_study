T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    total = sum(arr[:M])
    max_total = total
    min_total = total
    for x in range(N-M) :
        total += arr[x+M] - arr[x]
        max_total = max(max_total, total)
        min_total = min(min_total, total)
 
    print(f'#{test_case} {max_total-min_total}')


# T = int(input())
# for test_case in range(1, T + 1):
#     N, M = map(int, input().split())
#     arr = list(map(int, input().split()))
#     total_list = []
#     for x in range(N-M+1) :
#         total = 0 
#         for i in range(M) : 
#             total += arr[x + i]
#         total_list.append(total)
 
#     print(f'#{test_case} {max(total_list)-min(total_list)}')
