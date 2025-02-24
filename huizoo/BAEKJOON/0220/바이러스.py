N = int(input())
X = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(X):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

virus = [0]*(N+1)
q = []
q.append(1)
virus[1] = 1
while q:
    now = q.pop(0)
    for i in arr[now]:
        if not virus[i]:
            q.append(i)
            virus[i] = 1
print(virus.count(1)-1)