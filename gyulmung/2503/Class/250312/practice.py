import heapq

# 빈리스트에 입력시 정렬시키기
arr = []
heapq.heappush(arr, 1)
heapq.heappush(arr, 2)
heapq.heappush(arr, 4)
heapq.heappush(arr, 5)
heapq.heappush(arr, 63)
heapq.heappush(arr, 3)
print(arr)
for i in range(len(arr)):
    print(heapq.heappop(arr),end = ' ')
print()

# 원본데이터 유지 하면서 heap하기
arr = [3,4,2,5,6,6,6,6,4,343,34,2,2,1,]
lst = []
for i in range(len(arr)):
    heapq.heappush(lst, arr[i])
print(lst)
for i in range(len(arr)):
    print(heapq.heappop(lst), end = ' ')
print()

# heappush안쓰고 바로 바꾸기
heapq.heapify(arr)
print(arr)
for i in range(len(arr)):
    print(heapq.heappop(arr), end = ' ')