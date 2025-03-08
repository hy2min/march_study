K = int(input())

table = [
    [0, 1, 0, 0, 1, 0],
    [0, 0, 1, 0, 0, 1],
    [0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0],
]


def BFS(x):
    visited = [False] * 6
    queue = []
    current_queue = x
    queue.append(current_queue)
    visited[x] = True

    while queue:
        current_queue = queue.pop(0)
        print(current_queue, end=' ')
        for i in range(6):
            if table[current_queue][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

BFS(K)