# import sys
# sys.stdin = open("input.txt","r")

arr = [
    [0,0,1,1,0,1],
    [0,0,0,1,1,1],
    [0,0,0,0,1,1],
    [0,0,0,0,0,0],
    [1,0,0,0,0,1],
    [0,0,0,0,0,0],
]
used = [0] * 6

def dfs(num):

    print(num,end=' ')
    for i in range(6):
        if arr[num][i] == 1 and used[i] == 0:
            used[i] = 1
            dfs(i)

a = int(input())
used[a] = 1
dfs(a)