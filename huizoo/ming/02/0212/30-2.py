K = int(input())
table = [
    [0,0,1,0,2,0],
    [5,0,3,0,0,0],
    [0,0,0,0,0,7],
    [2,0,0,0,8,0],
    [0,0,9,0,0,0],
    [4,0,0,7,0,0],
]

visited = [False]*6

# cumulation = 0
# def dfs(n):
#     global cumulation
#     print(n, cumulation)
#     visited[n] = True
#     for i in range(6):
#         if table[n][i] >= 1 and not visited[i]:
#             cumulation += table[n][i]
#             dfs(i)
# dfs(K)

def dfs(n, current_weight):
    print(n, current_weight)
    visited[n] = True
    for i in range(6):
        if table[n][i] >= 1 and not visited[i]:
            current_weight += table[n][i]
            dfs(i, current_weight)
dfs(K, 0)

