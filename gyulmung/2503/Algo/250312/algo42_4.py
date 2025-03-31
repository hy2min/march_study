import sys
sys.stdin=open('input.txt','r')

n = int(input())
arr = [10, 40, 60]

def dfs(lev, Sum):
    global Min
    if Sum == n:
        Min = min(lev, Min)
        return

    if Min < lev:
        return

    for i in range(3):
        dfs(lev+1, Sum + arr[i])






Min = 1e8
dfs(0, 0)
print(Min)