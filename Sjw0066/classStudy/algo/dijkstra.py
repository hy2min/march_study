# 그래프 최소비용 알고리즘
# 다익스트라 /floid warshall /bellman ford

# 다익스트라 -> 비용이 양수여야함/ 시작점이 주어져야 함

# 음수일경우 못씀 ㅇㅇ / bellman ford 써야함 근데 음수 싸이클이 없어야함(따로 처리함)

# 시작점 x / floid warshall 쓰면 됨

# On2 과 Onlogn 방법 두개 있음  nlogn으로 외우셈


# 1. 다익스트라 On2 -> 인접행렬
'''
ABCDE
[
[0,3,inf,9,5],
[inf,0,7,inf,1],
[inf,inf,0,1,inf],
[inf,inf,inf,0,inf],
[inf,inf,1,inf,0],
]
'''
# 시작점에서 도착점 가는거랑
# 시작점 경유지 도착점 가는거랑 비교해서 비용값 업데이트
# 경유지 비용 적게 드는 순으로 거쳐서 보는걸로 확인
#
# name='ABCDE'
# inf=int(21e8)
# arr=[
# [0,3,inf,9,5],
# [inf,0,7,inf,1],
# [inf,inf,0,1,inf],
# [inf,inf,inf,0,inf],
# [inf,inf,1,inf,0],
# ]
# used=[0]*5
# used[0]=1 # 시작점 A 를 첫 경유지로 설정
# result=arr[0][:] # 첫번째 경유지를 시작점인 A로 놓았을경우
#
# def select_ky(): #경유지선택함수
#     Min=int(21e8)
#     Min_index=0
#
#     for i in range(5):
#         if used[i] == 0 and result[i]<Min:
#             Min=result[i]
#             Min_index=i
#
#     return Min_index
#
# def dijkstra():
#     # 경유지 선택
#     for i in range(4):
#         via=select_ky()
#         used[via] = 1
#     # 시작 -> 경유
#     # 시작 -> 경유 -> 도착 비교후 작은값 갱신
#         for j in range(5): # result 다 탐색하고 갱신하기
#             baro=result[j]
#             kyoung=result[via] + arr[via][j]
#             if baro>kyoung:
#                 result[j] = kyoung
#
# dijkstra()
# print(result)

# 2. nlogn 방식 -> 인접리스트
'''
5 7
0 1 3
0 3 9
0 4 5
1 2 7
1 4 1
2 3 1
4 2 1
0 3
'''
import heapq
name= "ABCDE"
N,M=map(int,input().split())
arr=[[] for _ in range(N)]

for _ in range(M):
    a,b,c=map(int,input().split()) # 시작,도착,비용
    arr[a].append((b,c))

st,ed=map(int,input().split()) # 결과를 위한 시작점 도착점

result=[21e8]*N
heap=[(0,st)]
result[st]=0

while heap:
    ky_cost,ky=heapq.heappop(heap)

    if result[ky] < ky_cost:continue

    for i in range(len(arr[ky])):
        dochack=arr[ky][i][0]
        dochack_cost=arr[ky][i][1]

        baro=result[dochack] # result 배열의 값 vs
        new=ky_cost+dochack_cost # 힙에서 빼온거 + 리스트에서 빼온거

        if new<baro:
            result[dochack] = new
            heapq.heappush(heap,(new,dochack))

print(*result)
print(result[ed])







































