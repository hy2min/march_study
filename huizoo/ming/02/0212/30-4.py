node = int(input())

table = [
    [0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0, 1],
    [0, 0, 1, 1, 0, 0],
]

# def BFS(n):
#     visited = [False]*6
#     queue = [n]
#     visited[n] = True
#     while queue:
#         current_queue = queue.pop(0)
#         print(current_queue)
#         for i in range(6):
#             if table[current_queue][i] == 1 and not visited[i]:
#                 queue.append(i)
#                 visited[i] = True

def BFS(n):
    visited = [False] * len(table)
    queue = [n]
    visited[n] = True
    head = 0  # 큐에서 현재 처리할 인덱스
    while head < len(queue):
        current = queue[head]
        print(current)
        for i in range(len(table)):
            if table[current][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True
        head += 1

BFS(node)