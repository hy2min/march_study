# import sys
# sys.stdin = open("input.txt","r")
import heapq

T = int(input())
for tc in range(1,T+1):
    N, M = map(int,input().split())
    containers = list(map(int,input().split()))
    trucks = list(map(int,input().split()))
    trucks.sort()
    heap = []
    ans = 0

    for container in containers:
        heapq.heappush(heap, (-container,container))

    while len(trucks) > 0 and len(heap) > 0:

        truck = trucks[-1]
        container = heapq.heappop(heap)[1]

        if truck >= container:
            ans += container
            trucks.pop()

    print(f"#{tc} {ans}")
