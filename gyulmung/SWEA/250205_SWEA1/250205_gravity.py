def rotation(N, M):
    arr = []
    for i in range(N):
        count = 0
        for j in range(1 + i, N):
            if M[i] > M[j]:
                count += 1
        arr.append(count)
    Max_num = 0
    for i in range(len(arr)):
        if Max_num < arr[i]:
            Max_num = arr[i]
    return Max_num


test_case = int(input())
for i in range(1, test_case + 1):
    N = int(input()) # 각 케이스의 첫째줄에 방의 가로 길이
    M = list(map(int,input().split()))
    result = rotation(N, M)
    print(f"#{i} {result}")

# def rotation(N, M):
#     arr = []
#     for i in range(N):
#         count = 0
#         for j in range(1, N):
#             if M[i] > M[j]:
#                 count += 1
#         arr.append(count)
#     Max_num = 0
#     for i in range(len(arr)):
#         if Max_num < arr[i]:
#             Max_num = arr[i]
#     return Max_num
