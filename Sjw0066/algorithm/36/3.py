import heapq
N,M,P = map(int,input().split())
P-=1
arr=[[] for _ in range(N)]

for _ in range(M):
    a,b,c=map(int,input().split())
    arr[a-1].append((b-1,c))

answer=[0]*N

for st in range(N):
    heap=[]
    heapq.heappush(heap,(0,st))
    result=[21e8]*N
    result[st]=0


