import sys
sys.stdin = open("input.txt","r")

name = 'ABCDEF'
arr = [list(map(int,input().split())) for _ in range(6)]
path = [0]

def dfs(num):

    flag = 0

    for i in range(6):
        if arr[num][i] == 1:
            flag = 1
            path.append(i)
            dfs(i)
            path.pop()

    if not flag:
        print("".join(name[i] for i in path))

dfs(0)