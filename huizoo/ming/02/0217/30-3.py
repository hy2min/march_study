K = int(input())
table = [
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]

def bfs(x):
    visited = [0]*6
    q = []
    cq = x
    q.append(cq)
    visited[x] = 1

    while q:
        cq = q.pop(0)
        print(cq, end=' ')
        for i in range(6):
            if table[cq][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = 1

bfs(K)