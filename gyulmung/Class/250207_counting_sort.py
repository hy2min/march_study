# arr = [4, 7, 8, 1, 4, 6]
#
# # 1. DAT 만들기
# lst = [0]*10
# for i in range(len(arr)):
#     lst[arr[i]] += 1
# print(lst)
#
# # 2. 누적 값
# # for i in range(len(lst)-1):
# #     lst[i+1] = lst[i] + lst[i+1]
#
# for i in range(1, len(lst)):
#     lst[i] += lst[i-1]
#
# print(lst)
#
# # 3. 값 넣기
# temp = [0]*len(arr)
# for i in range(len(arr)):
#     lst[arr[i]] = lst[arr[i]]-1
#     temp[lst[arr[i]]] = arr[i]
# print(temp)

# # 연속되는 숫자 3개의 합이 가장 클 떄의 값을 출력해주세요.
# lst = [[4, 5, 2, 6, 7, 3, 1], [2, 9, 9, 6, 1, 6, 7]]
# Sum_Three = []
# for j in range(2):
#     for i in range(2, 7):
#         Sum_num = lst[j][i-2] + lst[j][i-1] + lst[j][i]
#         Sum_Three.append(Sum_num)
#
# print(max(Sum_Three))

# 3 4 5라는 패턴이 어느 좌표에 있는지 찾기
#
# arr = [list(map(int, input().split())) for _ in range(3)]
# target = list(map(int, input().split()))

# 재밌다 신난다 즐겁다

# arr=[list(map(int, input().split())) for _ in range(4)]
# lst = []
# Max = -1e8
# # 땅나누기
# def Divide_land(a, b):
#     Sum = 0
#     for i in range(2):
#         for j in range(3):
#             Sum += arr[i+a][j+b]
#     return Sum
#
# for i in range(3):
#     for j in range(2):
#         ret = Divide_land(i,j)
#         if ret > Max:
#             Max = ret
# print(Max)

#