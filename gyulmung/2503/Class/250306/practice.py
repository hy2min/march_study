from collections import deque

# topology sort 위상정렬 'BFS'
# 작업순서 판단할때 사용
name = ['CS', 'language', 'pjt', ' algo', 'data_structure', 'coding_test', 'developer']
arr = [[0,0,1,0,0,0,0],
       [0,0,0,1,1,0,0],
       [0,0,0,0,0,0,1],
       [0,0,0,0,0,1,0],
       [0,0,0,0,0,1,0],
       [0,0,0,0,0,0,1],
       [0,0,0,0,0,0,0],]

acc = [0]*7
used = [0]*7
# 사전 작업 개수 파악
for j in range(7):
    for i in range(7):
        if arr[i][j] == 1:
            acc[j] += 1

# 사전 작업 없이 바로 시작할 수 있는 작업은
# 큐에 넣고 + used에 1체크해주기
q = deque()
for i in range(7):
    if acc[i] == 0:
        used[i] = 1
        q.append(i)

# bfs돌리면서 작업순서 큐에 넣기
while q:
    now = q.popleft()
    print(name[now], end= " ")
    for i in range(7):
        if arr[now][i] == 1 and used[i] == 0:
            if acc[i] == 1:
                acc[i] = 0
                used[i] = 1
                q.append(i)
            else:
                acc[i] -= 1
