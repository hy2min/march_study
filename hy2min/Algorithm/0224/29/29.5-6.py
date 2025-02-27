arr = [
    [3,2,5,3],
    [7,6,1,6],
    [4,9,2,7],
]
times = list(map(int,input().split()))
def dfs(level):
    for i in range(3):
        arr[i][0] = arr[i+1][0]