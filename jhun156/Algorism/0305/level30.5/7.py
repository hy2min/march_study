# import sys
# sys.stdin = open("input.txt","r")

arr = list(map(int,input().split()))
cnt = 0
used = [0] * 5

def dfs(start,Sum):

    global cnt
    if Sum > 20:
        return
    if 10 <= Sum <= 20:
        cnt += 1

    for i in range(start,5):
        if used[i] == 0:
            used[i] = 1
            dfs(i+1,Sum+arr[i])
            used[i] = 0

dfs(0,0)
print(cnt)