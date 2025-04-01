# arr = [[3, 5, 4], [1, 1, 2], [1, 3, 9]]
# y, x = map(int, input().split())
#
# # directY = [1, -1, 0, 0]
# directX = [0, 0, 1, -1]
# Sum = 0
# for i in range(4):
#     dy = y + directY[i]
#     dx = x + directX[i]
#     if dy > 2 or dy < 0 or dx > 2 or dx < 0:
#         continue
#     Sum += arr[dy][dx]
# print(Sum)








arr = [ [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8],
        [1, 2, 9, 1, 2],
        [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8]]

# 위 아래 좌 우 에서 좌우로 3칸까지 떨어진 곳들의 합을 구하시오

y, x = map(int, input().split())

directY = [1, -1, 0, 0]
directX = [0, 0, 1, -1]
Sum = 0
for i in range(1, 4):
    for j in range(4):
        dy = y + directY[j] * i
        dx = x + directX[j] * i

        if 0 <= dy < 5 and 0 <= dx < 5:
            Sum += arr[dy][dx]
print(Sum)



