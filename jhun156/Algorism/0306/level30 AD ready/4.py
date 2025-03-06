# import sys
# sys.stdin = open("input.txt","r")

n = int(input())
arr = list(map(int,input().split()))
ans = []
num = 0
used= [0] * n

def dfs(level):

    global Min,num
    if level == 3:
        ans.append(num)
        return

    for i in range(n):
        if level == 2 and arr[i] == 0:
            continue
        else:
            if used[i] == 0:
                used[i] = 1
                num += arr[i] * (10 ** level)
                dfs(level+1)
                used[i] = 0
                num -= arr[i] * (10 ** level)

dfs(0)
Min = min(ans)
print(Min)