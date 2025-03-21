# 사회망 서비스(SNS)
import sys, copy
input = sys.stdin.readline


N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

visit = set()
Min = 1e9

def abc(now, level, visited):
    global Min
    if level > Min:
        return
    visited2 = copy.deepcopy(visited)
    for nxt in arr[now]:
        visited2.add(nxt)

    if len(visited2) == N:
        Min = min(Min, level)
        return

    for i in range(1, N+1):
        if i not in visited2:
            visited3 = copy.deepcopy(visited2)
            visited3.add(i)
            abc(i, level+1, visited3)

for i in range(1, N+1):
    visit.add(i)
    abc(i, 1, visit)
    visit.remove(i)

print(Min)
