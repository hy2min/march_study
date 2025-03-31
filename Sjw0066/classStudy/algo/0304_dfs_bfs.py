# from collections import deque
#
# n=int(input())
# arr=[[0]*n for _ in range(n)]
#
# y,x=map(int,input().split())
#
# arr[y][x] = 1
# q=deque()
# q.append((y,x))
# direct_y=[0,0,-1,1]
# direct_x=[1,-1,0,0]
# while q:
#     a,b=q.popleft()
#
#     for i in range(4):
#         dy=a+direct_y[i]
#         dx=b+direct_x[i]
#         if dy>n-1 or dy<0 or dx>n-1 or dx<0: continue
#         if arr[dy][dx] != 0 : continue
#
#         arr[dy][dx] = arr[a][b] + 1
#
#         q.append((dy,dx))
#
# print(arr[0][0])
#
# #치즈먹고 여자친구
#
# from collections import deque
# arr=[[0,0,0,0,0,0],
#      [1,1,0,0,1,0],
#      [1,0,0,0,1,0],
#      [0,0,0,0,0,0]]
# direct_y=[0,0,-1,1]
# direct_x=[1,-1,0,0]
#
# answer=0
#
# '''
# 남친은 0,0에 있음
# 여친은 3,5에 있음
# 3,0에 치즈 가게 있음
# 치즈 가게 들렀다가 가는 최단거리 출력
# '''
# boy=list(map(int,input().split()))
# cheese=list(map(int,input().split()))
# girl=list(map(int,input().split()))
# Min=21e8
# def bfs(now,ed,cnt):
#     global Min
#     visited=[[0]*6 for _ in range(4)]
#     visited[now[0]][now[1]] = 1
#     q=deque()
#     q.append((now[0],now[1],cnt))
#
#     while q:
#         y,x,cnt=q.popleft()
#         for i in range(4):
#             dy=y+direct_y[i]
#             dx=x+direct_x[i]
#             if dy>len(arr)-1 or dy<0 or dx>len(arr[1])-1 or dx<0:continue
#             if arr[dy][dx] == 1 : continue
#             if visited[dy][dx] == 1: continue
#             if dy == ed[0] and dx == ed[1]:
#                 return cnt + 1
#             visited[dy][dx] = 1
#             q.append((dy,dx,cnt+1))
#
# answer=bfs(boy,cheese,0) + bfs(cheese,girl,0)
# print(answer)

# 가장 큰섬 사이즈 출력
# 가장 작은섬 사이즈 출력
# 가장 큰섬에서 작은섬까지 최단거리

# from collections import deque
# from copy import deepcopy
# arr=[
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,1,0,0],
#     [0,0,1,1,1,0],
#     [0,0,0,1,0,0],
#     [0,0,0,1,0,0],
# ]
# backup= deepcopy(arr)
# cnt=0
# def bfs(y,x):
#     global cnt
#     cnt=0
#     q=deque()
#     visited=[[0]*6 for _ in range(6)]
#
#     q.append((y,x))
#     direct_y=[0,0,1,-1]
#     direct_x=[1,-1,0,0]
#
#
#     while q:
#         yy,xx=q.popleft()
#         arr[yy][xx] = 0
#         for i in range(4):
#             dy=direct_y[i]+yy
#             dx=direct_x[i]+xx
#             if dy>5 or dx>5 or dx<0 or dx<0:continue
#             if visited[dy][dx] == 1: continue
#             if arr[dy][dx] == 0 : continue
#             visited[dy][dx] = 1
#             q.append((dy,dx))
#             cnt+=1
# size=0
#
# for i in range(6):
#     for j in range(6):
#         if arr[i][j] == 1:
#             bfs(i,j)
#             size=cnt
#             break
# print(size)
#
# from collections import deque
#
# map=[
#     [0,0,1,0,0,1],
#     [0,0,1,0,0,1],
#     [0,1,1,1,0,0],
#     [0,0,1,0,0,0],
#     [1,0,0,0,1,0],
# ]
#
# island_cnt=0
# Max=-21e8
# Min=21e8
# answer=[]
# def bfs(y,x):
#     q=deque()
#     q.append((y,x))
#     map[y][x]=0
#     size=1
#     direct_y=[0,0,1,-1]
#     direct_x=[1,-1,0,0]
#     while q:
#         y,x=q.popleft()
#         for i in range(4):
#             dy=direct_y[i] + y
#             dx=direct_x[i] + x
#
#             if dy>4 or dy<0 or dx>5 or dx<0 : continue
#             if map[dy][dx] == 0 : continue
#
#             map[dy][dx]=0
#             q.append((dy,dx))
#             size+=1
#
#     return size
#
# for i in range(5):
#     for j in range(6):
#         if map[i][j] == 1:
#             answer.append(bfs(i,j))
#             island_cnt+=1
#
# print(f'최솟값 {min(answer)}')
# print(f'최대값 {max(answer)}')
# print(f'섬개수 {island_cnt}')

# 모의 소방 훈련
# from collections import deque
# N=int(input())
# arr=[list(input()) for _ in range(N)]
# first=list(map(int,input().split()))
#
# direct_y=[0,0,1,-1]
# direct_x=[1,-1,0,0]
#
# def bfs_to_fire_ex(st,ed):
#     q=deque()
#     cnt = 1
#     q.append((st[0],st[1],cnt))
#     visited=[[0]*N for _ in range(N)]
#     visited[st[0]][st[1]] = 1
#     while q:
#         y,x,level=q.popleft()
#         for i in range(4):
#             dy=direct_y[i] + y
#             dx=direct_x[i] + x
#             if dy>N-1 or dy<0 or dx>N-1 or dx<0:continue
#             if visited[dy][dx] == 1 : continue
#             if arr[dy][dx] == '#' or arr[dy][dx] == '$':continue
#             if dy==ed[0] and dx==ed[1]:
#                 return level
#             visited[dy][dx] = 1
#             q.append((dy,dx,level+1))
#
# def bfs_to_fire(st):
#     q = deque()
#     cnt = 1
#     q.append((st[0], st[1],cnt))
#     visited = [[0] * N for _ in range(N)]
#     visited[st[0]][st[1]] = 1
#     while q:
#         y, x ,level= q.popleft()
#         for i in range(4):
#             dy = direct_y[i] + y
#             dx = direct_x[i] + x
#             if dy > N - 1 or dy < 0 or dx > N - 1 or dx < 0: continue
#             if visited[dy][dx] == 1: continue
#             if arr[dy][dx] == '#' or arr[dy][dx] == 'A': continue
#             if arr[dy][dx] == "$":
#                 return level
#             visited[dy][dx] = 1
#             q.append((dy, dx,level+1))
# Min=21e8
# answer=0
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] == "A":
#             answer=bfs_to_fire_ex(first,(i,j)) + bfs_to_fire((i,j))
#             if Min>answer:
#                 Min=answer
# print(Min)

#a 50
#b 40
#c 99
#d 5
#e 25
#f 6
#g 37

# 서바이벌 선수와 전투력이 있을때
# a~f를 두 팀으로 만들어서 서바이벌 게임을 하고자 한다.
# 두 팀의 전투력 차이가 가장 적게하여 두 팀을 구성한다고 했을때
# 두 팀의 최소 전투력 차이는 몇이 되는가?
# 모든 선수는 서바이벌에 참가하며 1인팀도 가능합니다.
name='abcdefg'
power=[50,40,99,5,25,6,37]
used=[0]*7

sum_power=0

for i in range(len(power)):
    sum_power+=power[i]

Min=21e8

def abc(level,Sum,st):
    global Min

    against=sum_power-Sum
    gap=abs(Sum-against)
    Min=min(gap,Min)

    if level==6:
        return

    for i in range(st,7):
        if used[i] == 1 : continue
        used[i] = 1
        abc(level+1,Sum+power[i],i+1 )
        used[i] = 0

abc(0,0,0)
print(Min)







