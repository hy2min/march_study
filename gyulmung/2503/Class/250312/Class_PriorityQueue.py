# from queue import PriorityQueue - 알고리즘 PS 분야에서 안쓴다.
import  heapq
arr = []
heapq.heappush(arr, 4) # 리스트에 heap 자료구조의 규칙에 의거해서 자료를 저장
heapq.heappush(arr, 6)
heapq.heappush(arr, 1)
heapq.heappush(arr, 2)
heapq.heappush(arr, 3)
print(arr)
print(type(arr))

# for i in range(len(arr)):
#     print(heapq.heappop(arr), end = ' ') # heap 규칙에 따라 출력 nlogn

while arr:
    temp = heapq.heappop(arr)
    print(temp, end = ' ')
print()

# 원본데이터 남겨두고 우선순위 heap 넣기
arr=[3422, 5, 3, 1, 5]
heap=[]
for i in range(len(arr)):
    heapq.heappush(heap, arr[i])

for i in range(len(arr)):
    print(heapq.heappop(heap), end = ' ')
print()

# 한번에 heap 규칙으로 바꾸기
arr=[3422, 5, 3, 1, 5]
heapq.heapify(arr)
print(arr)
for i in range(len(arr)):
    print(heapq.heappop(arr), end = ' ')
print()

# Maxheap 구현하기(1)
arr = [3422, 5, 3, 1, 5]
heap=[]
for i in range(len(arr)):
    heapq.heappush(heap, -arr[i])
print(heap)
for i in range(len(arr)):
    # print(heapq.heappop(heap)*-1, end=' ')
    print(-heapq.heappop(heap), end = ' ')
print()

# Maxheap 구현하기(2)
arr = [3422, 5, 3, 1, 5]
heap=[]
for i in range(len(arr)):
    heapq.heappush(heap,(-arr[i], arr[i]))
print(heap)
for i in range(len(arr)):
    print(heapq.heappop(heap)[1], end = ' ')
print()

# Maxheap 구현하기(3)
arr = [3422, 5, 3, 1, 5]
heap=list(map(lambda x:-x, arr))
heapq.heapify(heap)
for i in range(len(arr)):
    print(-heapq.heappop(heap), end=' ')
print()

# arr=[(1,5), (1,9), (4,2)]
# 우선순위 조건 1. 첫번째 원소 내림차순
# 우선순위 조건 2. 두번째 원소 오름차순
# class + init 매직 매서드

class Node:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __lt__(self, other): # less than < (작다) : self: 앞에 놓여야하는 값 / other: 뒤에 값
        if self.a > other.a: return True
        if self.a < other.a: return False
        return self.b < other.b # self.a 와 other.a가 같을 때 실행됨

heap = []
heapq.heappush(heap,(1, 5))
heapq.heappush(heap,(1, 9))
heapq.heappush(heap,(4, 2))

arr=[(1,5), (1,9), (4,2)]
arr=list(map(lambda x: Node(x[0], x[1])), arr)
heapq.heappify(arr)

while heap:
    temp = heapq.heappop(heap)
    print(temp.a, temp.b)