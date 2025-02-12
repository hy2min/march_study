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







