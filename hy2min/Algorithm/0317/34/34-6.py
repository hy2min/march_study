import heapq

n = int(input())
heap = list(map(int,input().split()))
cnt = 0

heapq.heapify(heap)
storage = []

while len(heap) > 0:

    stone1 = heapq.heappop(heap)
    if stone1 in storage:
        break
    cnt += 1

    stone2 = heapq.heappop(heap)
    if stone2 in storage:
        break
    cnt += 1

    new_stone = stone2 * 2

    heapq.heappush(heap, new_stone)
    storage.append(new_stone)
print(cnt)