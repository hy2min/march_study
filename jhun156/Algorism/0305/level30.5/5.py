# import sys
# sys.stdin = open("input.txt","r")

name = input()
num = int(input())
N = len(name)
path = [0] * num

def dfs(level):

    if level == num:
        for i in range(num):
            print(path[i],end='')
        print()
        return

    for i in range(N):
        path[level] = name[i]
        dfs(level+1)

dfs(0)
