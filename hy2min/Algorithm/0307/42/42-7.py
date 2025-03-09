def dfs(level, Sum):
    global maxSum
    if Sum <= maxSum:
        return
    if level == n:
        if Sum % 10 == 0:
            maxSum = max(maxSum,Sum)
            return
        
    for i in range(len(arr)):
        if visited[i] == 0:
            visited[i] = 1
            
            dfs(level+1, Sum-arr[i])
            visited[i] = 0
            
price = [15,20,44,22,55,16,45]
maxSum = -21e8

arr = [price[ord(i)-97] for i in list(input())]
n = int(input())
visited = [0]*len(arr)

dfs(0,sum(arr))
print(maxSum)