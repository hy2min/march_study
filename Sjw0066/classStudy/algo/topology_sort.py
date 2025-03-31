# 위상정렬
# bfs랑 비슷한 원리임
# 작업순서를 정할때 사용함
# 과목간의 우선순위가 있을때 작업의 순서를 판단

# 인접행렬에 먼저 하고 나중에 할 수 있는 작업을 적기
# from collections import deque
# name='ABCDEFG'
# arr=[
#     [0,0,1,0,0,0,0],
#     [0,0,0,1,1,0,0],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,1,0],
#     [0,0,0,0,0,1,0],
#     [0,0,0,0,0,0,1],
#     [0,0,0,0,0,0,0],
# ]
#
# # 사전 작업 개수 acc 배열과
# # 작업을 이미 했는지 보기 위한 used배열 두개 만들기
#
# acc=[0]*7 #세로로 탐색해서 넣어주면 됨 ㅇㅇ
# used=[0]*7
#
# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[j][i] == 1 :
#             acc[i] += 1
# # q에 넣고 used 1 체크하기
# q=deque()
# for i in range(7) :
#     if acc[i] == 0:
#         used[i] = 1
#         q.append(i)
#
# # bfs돌리면서 작업순서 큐에넣기
# while q:
#     now=q.popleft()
#     print(name[now],end=" ")
#     for i in range(7):
#         if arr[now][i] == 1 and used[i] == 0 :
#             if acc[i] == 1:
#                 acc[i] = 0
#                 used[i] = 1
#                 q.append(i)
#             else:
#                 acc[i] -= 1

# 사이클이 있으면 사용하지못한다.

N,M = map(int,input().split())
lst=[[]*(N+1) for i in range(N+1)]

for i in range(M):
    a,b=map(int,input().split())
    lst[a].append(b)








