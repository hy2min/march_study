# # 트리의 순회(탐색),기본적으로 이진트리의 탐색임
# # 1.pre order (전위 순회)
# tree=" ABCDEFG"
#
# def preorder(now):
#
#     if now>len(tree)-1:
#         return
#
#     print(tree[now],end=" ")
#     preorder(now*2)
#     preorder(now*2+1)
#
# preorder(1)
# print()
# def postorder(now):
#
#     if now>len(tree)-1:
#         return
#
#
#     postorder(now*2)
#     postorder(now*2+1)
#     print(tree[now], end=" ")
#
# postorder(1)
# print()
# def inorder(now):
#     if now > len(tree) - 1:
#         return
#
#     inorder(now * 2)
#     print(tree[now], end=" ")
#     inorder(now * 2 + 1)
#
# inorder(1)
# print()
#
# # binary search tree - 자료구조 면접 준비
# # 그냥 타겟이 있나 배열 탐색 -> On 순회 돌아야됨
# # 이진트리 만들어서 하면 logn이 됨
#
# # 최악의 경우 logn과 그냥 같아져 버림
# # red black tree -> 데이터의 추가 삭제가 잦을경우, 메모리 한정된경우
# # 위의 알고리즘으로 바꾸기 가능
# # 임베디드 펌웨어 개발에 자주 쓰임
#
# # b-tree 대용량 데이터 처리에 사용됨
# # 노드에 여러개의 값을 저장하는 형태의 트리
# # db에서 사용시 적절한 알고리즘임 / 추가삭제 용이
#
# # b-tree
#
# tree=[0]*20
# lst=[4,2,9,7,15,1,10,3]
#
# # 입력된 값(lst) 트리의 형태로 저장
# def insert(value):
#     now=1 #내가 저장할 인덱스
#     while 1:
#         if tree[now]==0:
#             tree[now] = value
#             return
#
#         if tree[now] >= value:
#             now=now*2
#         else :
#             now=now*2+1
#
# for i in lst:
#     insert(i)
#
# n=int(input())
#
# # 입력받은값 트리에 있나없나 보기
#
# def search(target):
#     now=1
#     while 1:
#         if tree[now] == 0 or now>len(tree)-1 : return 0
#
#         if tree[now] == target:
#             return 1
#         if tree[now] >= target:
#             now=now*2
#         else:
#             now=now*2+1
#
# answer=search(n)
#
# if answer:
#     print('있음')
# else:
#     print('없음')

# heap 자료구조 - 원리 반드시 이해/ 코드 구현 이해
# 다익스트라, 우선순위큐 할때 많이 나옴 ㅇㅇ..

# 우선순위가 가장 높은 자료를 우선으로 출력
# NlogN의 속도

# 최대힙 (기본)  큰값우선
# 최소힙 작은값 우선
# 부모랑 자식 사이만 보면됨 ㅇㅇ

arr=[4,1,6,3,2,8,9]
heap=[0]*20
hindex=1
def minheap(num,now):
    global hindex
    heap[hindex] = num
    now=hindex
    hindex+=1
    while 1:
        parent=now//2

        if parent==0:break

        if heap[parent]<=heap[now]:break

        heap[parent],heap[now] = heap[now],heap[parent]
        now=parent

for i in range(len(arr)):
    minheap(arr[i],i+1)
print(heap)


def top():
    return heap[1]

def Pop():
    global hindex
    hindex-=1
    heap[1]=heap[hindex]
    heap[hindex] = 0
    now=1

    while 1:
        left=now*2
        right=left+1

        if right<hindex and heap[left] < heap[right]: left=right
        if left>=hindex or heap[now] > heap[left]:break







for i in range(len(arr)):
    print(top(),end=" ")
    Pop()


