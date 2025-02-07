# arr = [[3, 5, 4], [1, 1, 2], [1, 3, 9]]
# y, x = map(int, input().split())
#
# direct_x=[1,0,-1,0]
# direct_y=[0,1,0,-1]
# sum1=0
#
# for i in range(4):
#     dy=y+direct_y[i]
#     dx=x+direct_x[i]
#     if dx<0 or dx>2 or dy<0 or dy>2:
#         continue
#     sum1+=arr[dy][dx]
# print(sum1)
#
# '''
# 파이썬에서만 되는거 있긴 함
# '''
# arr = [[3, 5, 4], [1, 1, 2], [1, 3, 9]]
# y, x = map(int, input().split())
#
# sum2=0
# for i,j in (-1,0),(1,0),(0,-1),(0,1):
#     dy,dx=y+i,x+j
#     if 0<=dy<3 and 0<=dx<3:
#         sum1+=arr[dy][dx]
# print(sum2)

arr = [ [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8],
        [1, 2, 9, 1, 2],
        [3, 5, 4, 5, 6],
        [1, 1, 2, 7, 8]]

y,x=map(int,input().split())
#
# direct_y=[-1,1,1,-1]
# direct_x=[-1,-1,1,1]
#
# mul=1
# for i in range(len(direct_x)):
#     dy=y+direct_y[i]
#     dx=x+direct_x[i]
#     if dy<0 or dy>4 or dx<0 or dx>4:
#         continue
#     mul *= arr[dy][dx]
#
# print(mul)

'''
위아래 좌우 3칸 떨어진 곳 합
'''

# arr = [ [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8],
#         [1, 2, 9, 1, 2],
#         [3, 5, 4, 5, 6],
#         [1, 1, 2, 7, 8]]
#
# # 위 아래 좌 우로 3칸까지 떨어진 곳들의 합을 구하시오
# y,x=map(int,input().split())
# directy=[0,0,-1,1]
# directx=[1,-1,0,0]
# Sum=0
# for i in range(4):
#         for power in range(1,4):
#                 dy=y+directy[i]*power
#                 dx=x+directx[i]*power
#                 if dy<0 or dx<0 or dy>4 or dx>4: continue
#                 Sum+=arr[dy][dx]
# print(Sum)


