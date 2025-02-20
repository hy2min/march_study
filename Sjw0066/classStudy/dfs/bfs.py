# from collections import deque

# name="ABCDEF"
#
# arr=[
#     [0,1,1,0,0,0],
#     [0,0,0,1,1,0],
#     [0,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
# ]
#
# def bfs(start):
#     q=deque()
#     q.append(start)
#
#     while q:
#         now=q.popleft()
#         print(name[now],end=" ")
#         for i in range(6):
#             if arr[now][i] == 1:
#                 q.append(i)
#
# bfs(0)
#
# name="BACD"
#
# arr=[
#     [0,0,0,1],
#     [1,0,1,0],
#     [1,0,0,1],
#     [0,0,0,0],
# ]
#
# used=[0]*4
#
#
# def bfs(start):
#     q=deque()
#     q.append(start)
#
#     while q:
#         now=q.popleft()
#         print(name[now],end=" ")
#         for i in range(4):
#             if used[i] == 1: continue
#             if arr[now][i] == 1:
#                 used[i] = 1
#                 q.append(i)
# used[1]=1
# bfs(1)

# from collections import deque
# import copy
#
# name="ABCD"
# arr=[
#     [0,1,1,0],
#     [0,0,1,1],
#     [0,1,0,1],
#     [0,0,0,0],
# ]
#
# cnt=0
#
# def bfs(start):
#     global cnt
#     q=deque()
#     used=[0]*4
#     used[start] = 1
#     q.append((start,used))
#
#     while q:
#         now, path = q.popleft()
#         if now==3:
#             cnt+=1
#
#         for i in range(4):
#             if arr[now][i] == 1 and path[i] == 0:
#                 used=copy.deepcopy(path)
#                 used[i] = 1
#                 q.append((i,used))
#
# bfs(0)
# print(cnt)

# FLOOD FILL (bloom , virus) 등

"""
4 x 4 사이즈 화단이 있음.
씨앗이 아무데나 떨어져서 퍼질거임
하루에 위아래좌우
특정 좌표가 꽃피는 날짜 구해라 or 다피는 날 언제임? 같은거 나옴
"""
# from collections import deque
#
#
# n=int(input())
# y1,x1=map(int,input().split())
#
# arr=[[0]*n for _ in range(n)]
# arr[y1][x1] = 1
# def bfs(i,j):
#     q=deque()
#     q.append((i,j))
#
#     direct_y=[0,0,1,-1]
#     direct_x=[1,-1,0,0]
#
#     while q:
#         y,x=q.popleft()
#
#         for i in range(4):
#             dy=direct_y[i]+y
#             dx=direct_x[i]+x
#
#             if dy<0 or dy>n-1 or dx<0 or dx>n-1:continue
#             if arr[dy][dx] !=0:continue
#             arr[dy][dx] = arr[y][x] + 1
#             q.append((dy,dx))
#
# bfs(y1,x1)
# for i in arr:
#     print(i)
# # print()
# from collections import deque
#
# N=int(input())
# y1,x1=map(int,input().split())
#
# arr=[[0]*N for _ in range(N)]
#
# def bfs(i,j):
#     q=deque()
#     q.append((i,j))
#     direct_y=[0,0,1,-1]
#     direct_x=[1,-1,0,0]
#     arr[i][j] = 1
#     while  q:
#         y,x = q.popleft()
#         for i in range(4):
#             dy=direct_y[i]+y
#             dx=direct_x[i]+x
#             if dy>N-1 or dy<0 or dx>N-1 or dx<0:continue
#             if arr[dy][dx] != 0: continue
#             arr[dy][dx] = arr[y][x] + 1
#             q.append((dy,dx))
#
# bfs(y1,x1)
# print(arr[0][1])
#
# from collections import deque
# N=int(input())
#
# y1,x1=map(int,input().split())
# y2,x2=map(int,input().split())
# arr=[[0]*N for _ in range(N)]
#
# def bfs(i1,j1,i2,j2):
#     q=deque()
#     q.append((i1,j1))
#     q.append((i2,j2))
#     direct_y=[0,0,1,-1]
#     direct_x=[1,-1,0,0]
#     arr[i1][j1]=1
#     arr[i2][j2]=1
#     while q:
#         y1,x1=q.popleft()
#         y2,x2=q.popleft()
#         for i in range(4):
#             dy1=direct_y[i] + y1
#             dx1=direct_x[i] + x1
#             dy2=direct_y[i] + y2
#             dx2=direct_x[i] + x2
#             if dy1>N-1 or dy1<0 or dx1>N-1 or dx1<0 : continue
#             if dy2>N-1 or dy2<0 or dx2>N-1 or dx2<0 : continue
#             if arr[dy1][dx1] != 0 or arr[dy2][dx2] != 0 : continue
#             arr[dy1][dx1] = arr[y1][x1] +1
#             arr[dy2][dx2] = arr[y2][x2] +1
#             q.append((y1,x1))
#             q.append((y2,x2))
#
#
# bfs(y1,x1,y2,x2)
#
# Max=0
# for i in arr:
#     Max=max(Max,max(i))
#     print(i)
# print(Max)
#
# from collections import deque
# # 미로 찾기
# # 0,0 에서 출발해서 3,3까지 도착하고자 한다.
# # 도착이이 가능한지 불가능 한지 출력해 주세요
# arr=[
# [0,0,0,0],
# [1,0,1,1],
# [1,0,1,0],
# [0,0,0,0]]
#
# directy=[0,0,-1,1]
# directx=[-1,1,0,0]
#
# visited=[[0]*4 for _ in range(4)]
# visited[0][0]=1
#
# q=deque()
# q.append((0,0))
# flag=0
# while q:
#     y,x=q.popleft()
#     for i in range(4):
#         dy=y+directy[i]
#         dx=x+directx[i]
#         if dy<0 or dx<0 or dy>3 or dx>3: continue
#         if arr[dy][dx]==1: continue
#         if visited[dy][dx]==1: continue
#         visited[dy][dx]=1
#         if dy==3 and dx==3:
#             flag=1
#             break
#         q.append((dy,dx))
#
# if flag:
#     print("도착가능")
# else:
#     print("도착 불가능")
















