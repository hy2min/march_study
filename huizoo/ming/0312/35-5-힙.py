import heapq

def ugly_numbers(n):
    heap = []
    heapq.heappush(heap, 1)
    seen = {1}
    primes = [2, 3, 5]
    ugly = []

    while len(ugly) < n:
        num = heapq.heappop(heap)
        ugly.append(num)

        for prime in primes:
            new_num = num * prime
            if new_num not in seen:
                heapq.heappush(heap, new_num)
                seen.add(new_num)

    return ugly

n = int(input())
arr = list(map(int, input().split()))

max_n = max(arr)
ugly_list = ugly_numbers(max_n)

for i in arr:
    print(ugly_list[i-1], end=' ')
