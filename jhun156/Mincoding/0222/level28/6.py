# import sys
# sys.stdin = open("input.txt","r")
# level은 예시 이미지와 다를 수 있음
# 종료 조건 used 1 카운트

N = 8
name = input()
arr = [list(map(int,input().split())) for _ in range(N)]
used = [0] * N
path = [0]
used[0] = 1

def dfs(num):

    tmp = used.count(1)
    if tmp == 8:
        return

    for next in range(N):
        if arr[num][next] == 1 and used[next] == 0:
            used[next] = 1
            path.append(next)
            dfs(next)

dfs(0)
for i in range(N):
    print(name[path[i]],end='')
