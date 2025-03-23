N, K = map(int, input().split())
arr = [[] for _ in range(K+1)]
grade = dict()
for _ in range(N):
    a, b = input().split()
    if a.isdecimal():
        a = int(a)
        if b.isdecimal():
            b = int(b)
            arr[a].append(b)
            arr[b].append(a)
        else:
            grade[a] = b
    else:
        grade[int(b)] = a

def search(x):
    visited[x] = 1
    for i in arr[x]:
        if i in grade:
            return grade[i]
        else:
            if visited[i]: continue
            return search(i)

for i in range(1, K+1):
    if i in grade:
        print(grade[i], end='')
    else:
        visited = [0] * (K + 1)
        print(search(i), end='')
