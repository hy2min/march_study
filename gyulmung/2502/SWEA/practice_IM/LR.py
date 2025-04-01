import sys

sys.stdin = open('input.txt', 'r')

T = int(input())


# def find_stone(y, x, arr, N):
#     direct_Y = [0, 0, 1, -1, 1, -1, -1, 1]
#     direct_X = [1, -1, 0, 0, 1, -1, 1, -1]
#     count = 0
#     count_T = 0
#     # 좌우 2칸 확인
#     for i in range(2):
#         for j in range(1, 4):
#             dy = direct_Y[i] * j + y
#             dx = direct_X[i] * j + x
#             if dx < 0 or dy < 0 or dx >= N or dy >= N:
#                 break
#             if j == 3 and arr[dy][dx] == 'o':
#                 count = 0
#                 break
#             elif arr[dy][dx] != 'o':
#                 break
#             else:
#                 count +=1
#     if count == 4:
#         count_T += 1
#
#     # 상하 2칸 확인
#     for i in range(2, 4):
#         for j in range(1, 3):
#             dy = direct_Y[i] * j + y
#             dx = direct_X[i] * j + x
#             if dx < 0 or dy < 0 or dx >= N or dy >= N:
#                 break
#             if j == 3 and arr[dy][dx] == 'o':
#                 count = 0
#                 break
#             elif arr[dy][dx] != 'o':
#                 break
#             else:
#                 count += 1
#     if count == 4:
#         count_T += 1
#
#     # 오른 대각선확인
#     for i in range(4, 6):
#         for j in range(1, 3):
#             dy = direct_Y[i] * j + y
#             dx = direct_X[i] * j + x
#             if dx < 0 or dy < 0 or dx >= N or dy >= N:
#                 break
#             if j == 3 and arr[dy][dx] == 'o':
#                 count = 0
#                 break
#             elif arr[dy][dx] != 'o':
#                 break
#             else:
#                 count += 1
#     if count == 4:
#         count_T += 1
#
#
#     # 왼 대각선 확인
#     for i in range(6, 8):
#         for j in range(1, 3):
#             dy = direct_Y[i] * j + y
#             dx = direct_X[i] * j + x
#             if dx < 0 or dy < 0 or dx >= N or dy >= N:
#                 break
#             if j == 3 and arr[dy][dx] == 'o':
#                 count = 0
#                 break
#             elif arr[dy][dx] != 'o':
#                 break
#             else:
#                 count += 1
#     if count == 4:
#         count_T += 1
#
#     return count_T

for test in range(1, T + 1):
    N = int(input())

    arr = [list(map(str, input().split())) for _ in range(N)]
    result = 0
    co = 0
    count_T =0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                direct_Y = [0, 0, 1, -1, 1, -1, -1, 1]
                direct_X = [1, -1, 0, 0, 1, -1, 1, -1]
                count = 0
                # 좌우 2칸 확인
                for a in range(2):
                    for b in range(1, 4):
                        dy = direct_Y[a] * b + i
                        dx = direct_X[a] * b + j
                        if dx < 0 or dy < 0 or dx >= N or dy >= N:
                            break
                        if arr[dy][dx] != 'o':
                            break
                        else:
                            count += 1
                if count >= 4:
                    count_T += 1

                # 상하 2칸 확인
                for a in range(2, 4):
                    for b in range(1, 3):
                        dy = direct_Y[a] * b + i
                        dx = direct_X[a] * b + j
                        if dx < 0 or dy < 0 or dx >= N or dy >= N:
                            break
                        if arr[dy][dx] != 'o':
                            break
                        else:
                            count += 1
                if count >= 4:
                    count_T += 1

                # 오른 대각선확인
                for a in range(4, 6):
                    for b in range(1, 3):
                        dy = direct_Y[a] * b + i
                        dx = direct_X[a] * b + j
                        if dx < 0 or dy < 0 or dx >= N or dy >= N:
                            break
                        if arr[dy][dx] != 'o':
                            break
                        else:
                            count += 1
                if count >= 4:
                    count_T += 1

                # 왼 대각선 확인
                for a in range(6, 8):
                    for b in range(1, 3):
                        dy = direct_Y[a] * b + i
                        dx = direct_X[a] * b + j
                        if dx < 0 or dy < 0 or dx >= N or dy >= N:
                            break
                        if arr[dy][dx] != 'o':
                            break
                        else:
                            count += 1
                if count >= 4:
                    count_T += 1
    if count_T >= 1:
        print(f'#{test} YES')
    else:
        print(f'#{test} NO')


direct = [(0, 1), (1, 0), ]