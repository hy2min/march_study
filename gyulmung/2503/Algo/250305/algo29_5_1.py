arr = ['시작', 3, 1, 2, 1, 3, 2, 1, 2, 1, '도착']
N = int(input())
def dfs(now, jump):
    print(arr[now], end =' ')
    if arr[now] == '도착':
        return
    dfs(now+jump, arr[now+jump])
    print(arr[now], end=' ')

dfs(0, N)