from collections import deque
arr = [list(input()) for _ in range(4)]

A = []
C = []
D = []

for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            A.append(i)
            A.append(j)
        if arr[i][j] == 'C':
            C.append(i)
            C.append(j)
        if arr[i][j] == 'D':
            D.append(i)
            D.append(j)

# 1초 뒤 오른쪽으로 이동
if A[1] + 1 >= 3:pass
elif arr[A[0]][A[1]+1] != '_': pass
else:
    arr[A[0]][A[1]], arr[A[0]][A[1]+1] = arr[A[0]][A[1]+1], arr[A[0]][A[1]]
    A[1] += 1
if C[1] + 1 >= 3:pass
elif arr[C[0]][C[1]+1] != '_': pass
else:
    arr[C[0]][C[1]], arr[C[0]][C[1]+1] = arr[C[0]][C[1]+1], arr[C[0]][C[1]]
    C[1] += 1
if D[1] + 1 >= 3:pass
elif arr[D[0]][D[1]+1] != '_': pass
else:
    arr[D[0]][D[1]], arr[D[0]][D[1]+1] = arr[D[0]][D[1]+1], arr[D[0]][D[1]]
    D[1] += 1
# 2초 뒤 아래쪽으로 이동
if A[0] + 1 >= 4:pass
elif arr[A[0]+1][A[1]] != '_': pass
else:
    arr[A[0]][A[1]], arr[A[0]+1][A[1]] = arr[A[0]+1][A[1]], arr[A[0]][A[1]]
    A[0] += 1
if C[0] + 1 >= 4:pass
elif arr[C[0]+1][C[1]] != '_': pass
else:
    arr[C[0]+1][C[1]], arr[C[0]][C[1]] = arr[C[0]][C[1]], arr[C[0]+1][C[1]]
    C[0] += 1
if D[0] + 1 >= 4:pass
elif arr[D[0]+1][D[1]] != '_': pass
else:
    arr[D[0]+1][D[1]], arr[D[0]][D[1]] = arr[D[0]][D[1]], arr[D[0]+1][D[1]]
    D[0] += 1
# 3초 뒤 왼쪽으로 이동
if A[1] - 1 < 0:pass
elif arr[A[0]][A[1]-1] != '_': pass
else:
    arr[A[0]][A[1]], arr[A[0]][A[1]-1] = arr[A[0]][A[1]-1], arr[A[0]][A[1]]
    A[1] -= 1
if C[1] - 1 < 0:pass
elif arr[C[0]][C[1]-1] != '_': pass
else:
    arr[C[0]][C[1]], arr[C[0]][C[1]-1] = arr[C[0]][C[1]-1], arr[C[0]][C[1]]
    C[1] -= 1
if D[1] - 1 < 0:pass
elif arr[D[0]][D[1]-1] != '_': pass
else:
    arr[D[0]][D[1]], arr[D[0]][D[1]-1] = arr[D[0]][D[1]-1], arr[D[0]][D[1]]
    D[1] -= 1
# 4초 뒤 위쪽으로 이동
if A[0] - 1 < 0:pass
elif arr[A[0]-1][A[1]] != '_': pass
else:
    arr[A[0]-1][A[1]], arr[A[0]][A[1]] = arr[A[0]][A[1]], arr[A[0]-1][A[1]]
    A[0] -= 1
if C[0] - 1 < 0:pass
elif arr[C[0]-1][C[1]] != '_': pass
else:
    arr[C[0]-1][C[1]], arr[C[0]][C[1]] = arr[C[0]][C[1]], arr[C[0]-1][C[1]]
    C[0] -= 1
if D[0] - 1 < 0:pass
elif arr[D[0]-1][D[1]] != '_': pass
else:
    arr[D[0]-1][D[1]], arr[D[0]][D[1]] = arr[D[0]][D[1]], arr[D[0]-1][D[1]]
    D[0] -= 1
# 5초 뒤 오른쪽으로 이동
if A[1] + 1 >= 3:pass
elif arr[A[0]][A[1]+1] != '_': pass
else:
    arr[A[0]][A[1]], arr[A[0]][A[1]+1] = arr[A[0]][A[1]+1], arr[A[0]][A[1]]
    A[1] += 1
if C[1] + 1 >= 3:pass
elif arr[C[0]][C[1]+1] != '_': pass
else:
    arr[C[0]][C[1]], arr[C[0]][C[1]+1] = arr[C[0]][C[1]+1], arr[C[0]][C[1]]
    C[1] += 1
if D[1] + 1 >= 3:pass
elif arr[D[0]][D[1]+1] != '_': pass
else:
    arr[D[0]][D[1]], arr[D[0]][D[1]+1] = arr[D[0]][D[1]+1], arr[D[0]][D[1]]
    D[1] += 1

for i in arr:
    print(*i, sep = '')











# q = deque()

# for i in range(4):
#     for j in range(3):
#         if arr[i][j] != '_' and arr[i][j] != '#':
#             q.append((i, j, 0))
#             arr[i][j] = '_'
# print(q, arr)

# while 1:
#     y, x, level = q.popleft()
#     if level == 0:
#         if x + 1 > 0:
#             q.append(y, x, level+1)
#         x += 1
#         q.append(y, x, level+1)
#     if level == 1:
#         if x + 1 > 0:
#             q.append(y, x, level+1)
#         x += 1
#         q.append(y, x, level+1)
#     if level == 2:
#         if x + 1 > 0:
#             q.append(y, x, level+1)
#         x += 1
#         q.append(y, x, level+1)
#     if level == 3:
#         if x + 1 > 0:
#             q.append(y, x, level+1)
#         x += 1
#         q.append(y, x, level+1)
#     if level == 5:
#         if x + 1 > 0:
#             q.append(y, x, level+1)
#         x += 1
#         q.append(y, x, level+1)