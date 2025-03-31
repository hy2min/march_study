# # 위아래좌우 좌표들의 합이 가장 큰 곳의 합과. 좌표값 출력하기
#
# arr=[[1,2,3,4],
#     [1,2,9,4],
#     [1,9,3,9],
#     [1,2,9,4]]
#
# # 복습
# Max = -1e8
# Max_y = 0
# Max_x = 0
#
# # 함수 내에서 방향을 조절하며 값을 출력한다.
# def Find_Max_values(y, x):
#     directY = [0, 0, -1, 1]
#     directX = [1, -1, 0, 0]
#     Sum = 0
#     for i in range(4):
#         dy = directY[i] + y
#         dx = directX[i] + x
#         if dy<0 or dx<0 or dy>3 or dx>3: continue
#         Sum += arr[dy][dx]
#     return Sum
#
#
# for i in range(4):
#     for j in range(4):
#         ret = Find_Max_values(i, j) # ret = Sum
#         if Max < ret:
#             Max = ret
#             Max_y = i
#             Max_x = i
# print(Max)
# print(Max_y, Max_x)

# ---------------------------------------------------------

# 모든 좌표로 부터 상하좌우 값 확인한다.

# 규칙 1.
# 기준 좌표로 부터 상하좌우의 범위가 배열범위를 넘어가면 무조건 0점처리

# 규칙 2.
# 1. 상하좌우의 합에서 기준좌표의 값을 뺀다.
# 1-1 상하좌우의 합에서 기준좌표의 값을 뺀 값이 음수라면 0점
# 1-2 상하좌우의 합에서 기준좌표의 값을 뺀 값이 짝수면 점수 2배하기

# 입력예제
# 테스트케이스의 개수를 입력 받는다.\
# 배열의 크기 N을 입력받은후 N * N 사이즈 배열에 들어갈 값을 입력 받는다.

# 출력결과
# 상하좌우의 합중 Max값 출력하기


import sys
sys.stdin = open('input.txt', 'r')

Test = int(input())

def Find_Max(arr, y, x, N):
    Sum = 0
    directY = [0, 0, 1, -1]
    directX = [1, -1, 0, 0]

    for i in range(4):
        dy = directY[i] + y
        dx = directX[i] + x

        if dy<0 or dx < 0 or dy >= N or dx >= N:
            return 0
        Sum += arr[dy][dx]
        if (Sum - arr[y][x]) % 2 == 1:
            return 0
        else:
            return Sum *2



for i in range(1, Test + 1):
    Max = -1e8
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    y = N
    x = N
    for j in range(y):
        for k in range(x):
            ret = Find_Max(arr, j, k, N)
            if Max < ret:
                Max = ret
    print(f'#{i} {Max}')


















