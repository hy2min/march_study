import heapq

Q = int(input())
arr = list(map(int, input().split()))
N = max(arr)

heap = [1]
seen = {1}
num = (2, 3, 5)
ugly = []

for _ in range(N):
    num = heapq.heappop(heap)
    ugly.append(num)

    for k in (2, 3, 5):
        nxt = num * k
        if nxt not in seen:
            seen.add(nxt)
            heapq.heappush(heap, nxt)

for i in arr:
    print(ugly[i-1], end=' ')
