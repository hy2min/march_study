# lst=[[0]*7 for _ in range(2)]
#
# N=int(input())
#
# for i in range(4):
#     lst[0][i] = N+i
#     lst[1][7-i] = N-i
#
# print(lst)

N,M=map(int,input().split())
card=list(map(int,input().split()))
path=[0]*M
used=[0]*N
Min=21e8
Mul_list=[0]*(M)
answer=[]
def dfs(level,Mul):
    global answer,Min

    if level==M:
        if Min>Mul:
            Min=Mul
            answer=path[:]
        return

    for i in range(len(card)):
        if used[i] == 1 : continue
        path[level] = card[i]
        used[i] = 1
        dfs(level+1,Mul*card[i])
        used[i] = 0


dfs(0,1)
answer.sort()
print(*answer)
