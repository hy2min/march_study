import heapq

q = int(input())
k_lst = list(map(int, input().split()))

limit = max(k_lst)
ugly_numbers = []
heap = [1]
visited = set([1])

factors = [2, 3, 5]
cnt = 0

while cnt < limit:
    small = heapq.heappop(heap)
    ugly_numbers.append(small)
    cnt += 1

    for factor in factors:
        new_ugly = small * factor
        if new_ugly not in visited:
            visited.add(new_ugly)
            heapq.heappush(heap, new_ugly)

for i in k_lst:
    print(ugly_numbers[i-1], end=" ")