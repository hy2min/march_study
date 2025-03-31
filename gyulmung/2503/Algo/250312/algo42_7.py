import sys
sys.stdin = open('input.txt','r')

def dfs(lev, Sum):
    global Max
    if lev == n:
        if Sum % 10 == 0:
            Max = max(Max, Sum)
            return
        return

    for i in range(len(arr)):
        if visited[i] != 1:
            visited[i] = 1
            dfs(lev + 1, Sum - items[arr[i]])
            visited[i] = 0

items = [15, 20, 44, 22, 55, 16, 45]
arr = list(input())
O_sum = 0
for i in range(len(arr)):
    arr[i] = ord(arr[i]) - 97
    O_sum += items[arr[i]]

visited = [0]*len(arr)
n = int(input())
Max = -1e8
dfs(0, O_sum)
print(Max)