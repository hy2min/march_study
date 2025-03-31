import heapq
import sys
sys.stdin = open("input.txt", "r")
T=int(input())

def findboss(member):

    if parent[member] == member:
        return member

    ret=findboss(parent[member])
    parent[member]=ret
    return ret

def union(a,b):
    global flag
    bossA,bossB=findboss(a),findboss(b)

    if bossA==bossB:
        flag=0
        return

    flag=1
    parent[bossB]=bossA

for tc in range(1,T+1):
    N=int(input())
    x_lst=list(map(int,input().split()))
    y_lst=list(map(int,input().split()))
    E=float(input())
    heap=[]
    parent=list(range(N))

    for i in range(N):
        for j in range(i+1,N):
            cost=(((x_lst[i]-x_lst[j])**2+(y_lst[i]-y_lst[j])**2)*E)
            heapq.heappush(heap,(cost,i,j))

    total_cost=0
    while heap:
        flag=0
        cost,st,ed = heapq.heappop(heap)
        union(st,ed)

        if flag:
            total_cost+=cost

    print(f'#{tc} {round(total_cost)}')

