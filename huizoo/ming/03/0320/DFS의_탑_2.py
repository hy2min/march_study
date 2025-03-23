# Graph 순회
import sys
input = sys.stdin.readline

def preorder(x):
    if x <= N:
        visited[x] = 1
        print(x, end=' ')
        for nxt in arr[x]:
            if not visited[nxt]:
                visited[nxt] = 1
                preorder(nxt)

def postorder(x):
    if x <= N:
        visited[x] = 1
        for nxt in arr[x]:
            if not visited[nxt]:
                visited[nxt] = 1
                postorder(nxt)
        print(x, end=' ')

N, K = map(int, input().split())
S = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a].append(b)

for i in range(N+1):
    arr[i].sort(reverse=True)

visited = [0]*(N+1)
preorder(S)

print()

visited = [0]*(N+1)
postorder(S)
