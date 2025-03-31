# 숫자 6개 존재
# 인접 리스트로 풀이
# import sys
# sys.stdin = open("input.txt","r")

lst = [
    [],
    [3,5,6],
    [1,4],
    [5],
    [1],
    [1],
    [],
]

S,G = map(int,input().split())
# 출발, 도착
Min = 1000
visited = [0] * 7
visited[S] = 1
flag = 0

def dfs(num,level):

    global Min,flag
    if num == G:
        flag = 1
        if Min > level:
            Min = level
            return

    for next in lst[num]:
        if visited[next] == 0:
            visited[next] = 1
            dfs(next,level+1)

dfs(S,0)
if flag:
    print(Min)
else:
    print(0)