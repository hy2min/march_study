def max_min(N, M):
    Min_num = M[0]
    Max_num = 0
    for i in range(N):
        if Min_num > M[i]:
            Min_num = M[i]
        if Max_num < M[i]:
            Max_num = M[i]
    return Max_num - Min_num

test_case = int(input())

for i in range(1, test_case + 1):
    N = int(input())
    M = list(map(int, input().split()))

    result = max_min(N, M)

    print(f'#{i} {result}')

# def max_min(N, M):
#     Min_num = M[0]
#     Max_num = 0
#     for i in range(N):
#         if Min_num > M[i]:
#             Min_num = M[i]
#         if Max_num < M[i]:
#             Max_num = M[i]
#     return Max_num - Min_num