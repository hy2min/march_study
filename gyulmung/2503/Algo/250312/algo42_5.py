import sys
sys.stdin = open('input.txt','r')

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = int(input())

def dfs(lev, Sum):
    global cnt
    if lev == n:
        if Sum == 10:
            cnt += 1
            return
        return

    for i in range(9):
        dfs(lev + 1, Sum + arr[i])


cnt = 0
dfs(0, 0)
print(cnt)