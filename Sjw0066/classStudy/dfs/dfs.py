# 그 래 프
# 데이터의 관계를 저장하는 자료구조

# 알고리즘 : 문제를 효율적으로 해결하는 방법
# 자료구조 : 입력받은 데이터를 어떻게 저장하고 관리 할 것 인가?
# 어떤 규칙에 의거해서 입력 또는 출력을 할 것인가?

# 선형 : 리스트 , 스택 , 큐 , 연결 리스트(linked list)
# 비선형 : 트리,그래프

# 비선형 자료구조를 탐색하기 위해선 알고리즘을 사용한다.
# dfs , bfs
# name = ['Amy', 'Bob', 'Charles', 'Diane', 'Edger']
# arr=[
#     [0,1,0,0,0],
#     [0,0,1,0,0],
#     [0,0,0,0,0],
#     [0,0,1,0,1],
#     [1,0,1,0,0]]
# max_cnt=-21e8
# for i in range(5):
#     cnt=0
#     for j in range(5):
#         if arr[j][i] :
#             cnt+=1
#     if cnt>max_cnt:
#         max_cnt=cnt
#         a=i
#
# print(name[a])


# 인접행렬을 통해 형제 찾기 (부모먼저 찾기)
'''
1. 부모먼저 찾기 루트 노드의 경우 형제가 없다.
2. 부모의 row 에 1이 없으면 형제없음. 본인 아닌 1이 있으면 금마가 형제임
'''
# arr=[
#     [0,1,1,0,0,0],
#     [0,0,0,1,1,0],
#     [0,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
# ]
#
# name=['A','B','C','D','E','F']
#
# target=input()
# target_index=ord(target)-65
# bro=-1
# parents=-1
#
#
# for i in range(6):
#     if arr[i][target_index] == 1:
#         parents = i
#         break
# if parents==-1:
#     print('형제없음')
# else:
#     for i in range(6):
#         if arr[parents][i] == 1 and i != target_index:
#             bro=i
#             break
#     if bro == -1 :
#         print('형제없음')
#     else:
#         print(chr(bro+ord("A")))

# arr=[
#     [0,1,1,0,0,0],
#     [0,0,0,1,1,0],
#     [0,0,0,0,0,1],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
#     [0,0,0,0,0,0],
# ]
# name=['A','B','C','D','E','F']
#
# def dfs(now):
#     print(name[now],end=" ")
#
#     for i in range(6):
#         if arr[now][i] == 1:
#             dfs(i)
#
# dfs(0)

#인접 리스트 버전
# n,m=map(int,input().split())
# arr=[[] for _ in range(6)]
# for i in range(m):
#     a,b=map(int,input().split())
#     arr[a].append(b)
#
#
# def dfs(now):
#     print(chr(now+65),end=' ')
#     for i in arr[now]:
#         dfs(i)
#
# dfs(0)

# 트리모양 이었음
#########################################################################

# 1번씩만 탐색할 경우
#
# name = "ABCD"
# arr = [
#     [0, 1, 1, 0],
#     [0, 0, 1, 1],
#     [1, 1, 0, 1],
#     [0, 0, 0, 0]]
#
# used = [0] * 4
# answer = []
#
# def dfs(now):
#     global answer
#     answer.append(name[now])
#     for i in range(4):
#         if arr[now][i] == 1 and used[i] == 0:
#             used[i] = 1
#             dfs(i)
#
#
# used[0] = 1
# dfs(0)
# print(*answer)
#
#

# 모든 경우의 수 카운팅 (USED 배열 초기화)
#
# name='BACD'
# arr=[
#     [0,0,1,1],
#     [1,0,1,0],
#     [1,0,0,1],
#     [0,0,0,0]]
# used=[0]*4
#
# cnt=0
# def dfs(now):
#     global cnt
#     if now==3:
#         cnt+=1
#
#     for i in range(4):
#         if arr[now][i]==1 and used[i]==0:
#             used[i]=1
#             dfs(i)
#             used[i]=0
#
# used[1]=1
# dfs(1)
# print(cnt)

# 각 루트에 비용이 있을 시 Sum 매개변수

# name=['B','A','C','D']
# arr=[
#     [0,0,1,7],
#     [1,0,4,0],
#     [1,0,0,1],
#     [0,0,0,0],
# ]
#
# used=[0]*4
# cnt=0
# Min=21e8
# def dfs(now,Sum):
#     global cnt
#     global Min
#
#
#
#     if now==3:
#         if Min > Sum:
#             Min = Sum
#
#     for i in range(4):
#         if arr[now][i] and used[i]==0:
#             used[i]=1
#             dfs(i,Sum+arr[now][i])
#             used[i]=0
#
# used[1]=1
# dfs(1,0)
# print(Min)

# Sum global 버전

# name=['B','A','C','D']
# arr=[
#     [0,0,1,7],
#     [1,0,4,0],
#     [1,0,0,1],
#     [0,0,0,0],
# ]
#
# used=[0]*4
# cnt=0
# Min=21e8
# Sum=0
# def dfs(now):
#     global cnt
#     global Min
#     global Sum
#
#     if now==3:
#         if Min > Sum:
#             Min = Sum
#
#     for i in range(4):
#         if arr[now][i] and used[i]==0:
#             used[i]=1
#             Sum += arr[now][i]
#             dfs(i)
#             Sum -= arr[now][i]
#             used[i]=0
#
# used[1]=1
# dfs(1)
# print(Min)
#



# 인접리스트 무방향 그래프 최소비용
# name=['A','B','C','D']
#
# n,m=map(int,input().split())
# lst=[[] for _ in range(n)]
#
# def dfs(now,Sum):
#     global Min
#
#     if now==3:
#         if Min>Sum:
#             Min=Sum
#         return
#
#     for i in lst[now]:
#         if used[i[0]] == 1:
#             continue
#         used[i[0]] = 1
#         dfs(i[0],Sum+i[1])
#         used[i[0]] = 0
#
# for i in range(m):
#     used=[0]*n
#     st,ed,cost = map(int,input().split())
#     lst[st].append((ed,cost))
#     lst[ed].append((st,cost))
#
# Min=21e8
# used[0]=1
# dfs(0,0)
# print(Min)
'''




'''
# 위에서 부터 한칸 씩 내려오면서
# 숫자 한개씩을 선택합니다,
# 선택한 숫자들을 모두 더했을 때
# 합이 20 이상인 경우가 몇가지 인지 출력해 주세요

#
# arr= [
#     [4,5,2],
#     [-2,1,6],
#     [3,9,-4],
#     [3,5,2],
# ]
# cnt=0
#
# def floor(level,Sum):
#     global cnt
#
#     if level == 4 :
#         if Sum > 20:
#             cnt+=1
#         return
#
#     for i in range(3):
#         floor(level+1,Sum+arr[level][i])
#
# floor(0,0)
# print(cnt)
'''




'''
# 위에서 부터 한칸 씩 내려오면서
# 숫자 한개씩을 선택합니다.
# 계단을 밑으로 내려오면서 이동할 수 있는 범위는
# 7시방향 6시방향 5시방향 입니다.
# 선택한 숫자들을 모두 더했을 때
# 합이 30 이상인 경우가 몇가지 인지 출력해 주세요
#
# arr=[[3,5,9,6],
#      [7,-8,1,6],
#      [-10,2,3,9],
#      [5,1,2,8],
#      [4,7,1,8]]
#
# def dfs(level,Sum,now):
#     global cnt
#
#     if level==5:
#         if Sum>=30:
#             cnt+=1
#         return
#
#     for i in range(-1,2):
#         dx=now+i
#         if dx < 0  or dx >3 :
#             continue
#
#         dfs(level+1,Sum+arr[level+1][dx],dx)
#
# cnt=0
# path=[0]*5
# for i in range(4):
#     dfs(1,arr[0][i],i)
# print(cnt)

# 미로찾기
# 벽 과 왔던곳 체크하기
#
# arr=[
#     [0,0,0,0],
#     [1,0,1,0],
#     [1,0,1,0],
#     [0,0,0,0],
# ]
# visited=[[0]*4 for _ in range(4)]
# flag=0
# def dfs(y,x):
#     global flag
#
#     if y==3 and x==3:
#         flag=1
#         return
#
#     direct_y=[0,0,1,-1]
#     direct_x=[1,-1,0,0]
#
#     for i in range(4):
#         dy=y+direct_y[i]
#         dx=x+direct_x[i]
#         if dy<0 or dy>3 or dx<0 or dx>3: continue
#         if arr[dy][dx] == 1: continue
#         if visited[dy][dx] == 1: continue
#         visited[dy][dx]=1
#         dfs(dy,dx)
#
#         if flag==1:
#             return
#
# visited[0][0] = 1
# if flag:
#     print("탈출")
# else:
#     print('탈출불가')

# arr=[
#     [0,0,0,0,0,0],
#     [1,0,1,0,1,0],
#     [1,0,1,0,1,0],
#     [1,0,1,0,1,0],
#     [0,0,0,0,0,0],
# ] # N*M
#
# visited=[[0]*len(arr[0]) for _ in range(len(arr))]
# Min=21e8
# def dfs(y,x,cnt):
#     global Min
#
#     if cnt>Min:
#         return
#
#     if y==2 and x==3:
#         if Min>cnt:
#             Min=cnt
#         return
#
#     direct_y=[0,0,1,-1]
#     direct_x=[1,-1,0,0]
#
#     for i in range(4):
#         dy=direct_y[i]+y
#         dx=direct_x[i]+x
#
#         if dy>len(arr)-1 or dy<0 or dx>len(arr[i])-1 or dx<0:continue
#         if visited[dy][dx] == 1: continue
#         if arr[dy][dx] == 1: continue
#         visited[dy][dx] =1
#         dfs(dy,dx,cnt+1)
#         visited[dy][dx] = 0
#
# visited[0][0]=1
# dfs(0,0,0)
# print(Min)
#
# arr=[
#     [4,8,1],
#     [9,2,6],
#     [3,5,7],
# ]
#
# Max=-21e8
#
# def dfs(y,x,level,lst):
#     global Max
#
#     for i in range(5):
#         dy = direct_y[i] + y
#         dx = direct_x[i] + x
#         if dy < 0 or dy > 2 or dx < 0 or dx > 2: continue
#         lst[dy][dx] = (lst[dy][dx] * 7) % 10
#
#     if level==2:
#         Sum=0
#         for i in range(3):
#             for j in range(3):
#                 Sum+=lst[i][j]
#         if Sum>Max:
#             Max=Sum
#         return
#
#
#
#     for i in range(3):
#         for j in range(3):
#
#             dfs(i,j,level+1,lst)
#
#
#
# direct_y=[0,0,0,-1,1]
# direct_x=[-1,0,1,0,0]
#
# for i in range(3):
#     for j in range(3):
#         dfs(i,j,0,arr)
#
# print(Max)

# 개발을 착수한 곳의 위 아래 좌 우 그리고 자기자신의 좌표의 값이
# *7 한 후 %10 한 값으로 바뀐다고 합니다.
# 총 3번의 개발 후 3*3 사이즈의 땅의가치를 모두 더했을떄
# 최대 이익은 몇일까요? (중복가능)
import copy
arr=[[4,8,1],[9,2,6],[3,5,7]]
Max=-21e8
def digging(y,x):
    directy=[0,0,-1,1,0]
    directx=[1,-1,0,0,0]
    for i in range(5):
        dy=directy[i]+y
        dx=directx[i]+x
        if dy<0 or dx<0 or dy>2 or dx>2: continue
        arr[dy][dx]=(arr[dy][dx]*7)%10

def getSum():
    global arr
    Sum=0
    for i in range(3):
        for j in range(3):
            Sum+=arr[i][j]
    return Sum

def dfs(level):
    global arr,Max
    backup=copy.deepcopy(arr)
    if level==3:
        result=getSum()
        Max=max(result,Max)
        return

    for i in range(3):
        for j in range(3):
            digging(i,j)
            dfs(level+1)
            arr=copy.deepcopy(backup)

dfs(0)
print(Max)









