# # 힙 같은경우 우선순위가 높은것 먼저 뽑음 기본값 min heap
# # 완전이진트리였음 ㅇㅇ
# # 힙은 우선순위큐의 일종 ㅇㅇ
# # from queue import PriorityQueue 가 있긴한데 안씀 느림 ㅇㅇ
import heapq
# arr=[]
# heapq.heappush(arr,4)
# heapq.heappush(arr,6)
# heapq.heappush(arr,1)
# heapq.heappush(arr,2)
# heapq.heappush(arr,3)
# heapq.heappush(arr,8)
#
# # list에 값을 집어 넣을때 힙의 규칙대로 집어넣음
# print(arr) #[1, 2, 4, 6, 3, 8]
# print(type(arr)) # <class 'list'>
# '''
# for i in range(len(arr)):
#     print(heapq.heappop(arr),end=" ") # 1 2 3 4 6 8 알아서 힙 규칙대로 출력
# '''
# # 시간 복잡도 nlogn 으로 된다.
# # min heap 만 지원됨
# # 원본데이터 날아감
# while arr:
#     temp=heapq.heappop(arr)
#     print(temp,end=" ") # 1 2 3 4 6 8
#


# arr=[3422,5,3,1,5]
# # 하나씩 바꾸기
# heap=[]
# for i in range(len(arr)):
#     heapq.heappush(heap,arr[i])
#
# for i in range(len(heap)):
#     print(heapq.heappop(heap),end=" ") # 1 3 5 5 3422
#
# # 한번에 arr 자체를 힙으로 바꾸기
# heapq.heapify(arr)
# print(arr) # [1, 5, 3, 5, 3422]
#
# # Maxheap 구현 방법
# # 1.
# arr=[3422,5,3,1,5]
# heap=[]
#
# for i in range(len(arr)):
#     heapq.heappush(heap,-arr[i])
# print(heap) # [-3422, -5, -3, -1, -5]
#
# while heap:
#     print(-heapq.heappop(heap),end=" ") # 3422 5 5 3 1

# # heapify 는 음수붙여서 새로 리스트 만들어야됨
# # 2. 튜플로 저장하기
# arr=[3422,5,3,1,5]
# heap=[]
#
# for i in range(len(arr)):
#     heapq.heappush(heap,(-arr[i],arr[i]))
# print(heap) # [(-3422, 3422), (-5, 5), (-3, 3), (-1, 1), (-5, 5)]
#
# for i in range(len(heap)):
#     print(heapq.heappop(heap)[1],end=" ") # 3422 5 5 3 1
#
# # 3. heapify
# arr=[3422,5,3,1,5]
# arr=list(map(lambda x:-x,arr))
# heapq.heapify(arr)
# for i in range(len(arr)):
#     print(-heapq.heappop(arr),end=" ") # 3422 5 5 3 1

'''
카드 정렬하기

정렬된 두 묶음의 숫자 카드가 있다고 하자. 각 묶음의 카드의 수를 A, B라 하면 보통 두 묶음을 합쳐서

하나로 만드는 데에는 A+B 번의 비교를 해야 한다. 

이를테면, 20장의 숫자 카드 묶음과 30장의 숫자 카드 묶음을 합치려면 50번의 비교가 필요하다.

매우 많은 숫자 카드 묶음이 책상 위에 놓여 있다. 이들을 두 묶음씩 골라 서로 합쳐나간다면, 

고르는 순서에 따라서 비교 횟수가 매우 달라진다.

예를 들어 10장, 40장, 20장의 묶음이 있을때 10장과 40장을 합친 뒤, 

합친 50장 묶음과 20장을 합친다면  (10 + 40) + (50 + 20) = 120 번의 비교가 필요할 것이다.

그러나 10장과 20장을 합친 뒤, 합친 30장 묶음과 40장을 합친다면

(10 + 20) + (30 + 40) = 100번의 비교가 필요하다. 더 효율적인 방법이라고 할수 있을것이다.

N개의 숫자 카드 묶음의 각각의 크기가 주어질 때, 최소한 몇 번의 비교가 필요한지를 

구하는 프로그램을 작성하시오.


입력
첫째 줄에 N이 주어진다. (1 ≤ N ≤ 100,000) 이어서 N개의 줄에 걸쳐 

숫자 카드 묶음의 각각의 크기가 주어진다. 

숫자 카드 묶음의 크기는 1,000보다 작거나 같은 양의 정수이다.


출력
첫째 줄에 최소 비교 횟수를 출력한다.

입력
4
50
20
70
30

출력
320


입력
3
10
20
40

출력
100

'''
# N=int(input())
# heap=[]
# for i in range(N):
#     heapq.heappush(heap,int(input()))
# answer=0
#
# while len(heap)>1:
#     a=heapq.heappop(heap)
#     b=heapq.heappop(heap)
#     c=a+b
#     answer+=c
#     heapq.heappush(heap,c)
#
# print(answer)
#
# # 우선순위가 조건 2개일때는 class 정의해야됨
#
# # arr=[(1,5),(1,9),(4,2)]
# # 1. 첫 원소 내림
# # 2. 두번째 올림
#
# import heapq
# class Node:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#
#     def __lt__(self, other): # less then (작다)
#         if self.a > other.a:return True
#         if self.a < other.a:return False
#         return self.b<other.b
#
#
# # heap=[]
# # heapq.heappush(heap,Node(1,5)) # heapq 내부에서 크기비교 연산할때
# # heapq.heappush(heap,Node(1,9))
# # heapq.heappush(heap,Node(4,2))
#
# heap=[(1,5),(1,9),(4,2)]
# heap=list(map(lambda x:Node(x[0],x[1]),heap))
# heapq.heapify(heap)
#
# while heap:
#     temp=heapq.heappop(heap)
#     print(type(temp.a),temp.b)

# 프로그래머스 더 맵게

def solution(scoville, K):

    heap=heapq.heapify(scoville)
    return answer


answer=solution()
print(answer)







