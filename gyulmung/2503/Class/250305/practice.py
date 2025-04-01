#preorder
arr = ' ABCDEFG'
def preorder(now):
    if now > len(arr)-1:
        return

    print(arr[now], end=" ")
    preorder(now*2)
    preorder(now*2+1)

preorder(1)

#postorder
def postorder(now):
    if now > len(arr) - 1:
        return

    postorder(now * 2)
    postorder(now * 2 + 1)
    print(arr[now], end=" ")

postorder(1)

#inorder
def inorder(now):
    if now > len(arr) - 1:
        return

    inorder(now * 2)
    print(arr[now], end=" ")
    inorder(now * 2 + 1)

inorder(1)

arr1=[0]*20 # 트리의 형태로 저장할 1차원 배열 만들기
lst = [4, 2, 9, 7, 15, 1]

def insert(value):
    now = 1 # 내가 저장할 index 값
    while 1:
        if arr1[now] == 0:
            arr1[now] = value
            return
        if arr1[now] < value:
            now = now*2+1
        else:
            now = now * 2

def search(target):
    now = 1
    while 1:
        if now >= len(arr1):
            return 0
        if arr1[now] == 0:
            return 0

        if arr1[now] == target: return 1
        if arr1[now] < target:
            now = now*2+1
        else:
            now = now*2

# 입력된 값(lst) 트리의 형태로 저장
# insert() 함수만들기
for i in lst:
    insert(i)
# n = int(input())
n=15
ans = search(n)
if ans:
    print('존재')
else:
    print('없음')


arr2=[6, 4, 1, 4, 7, 8, 1]
heap = [0]*20
hindex=1

def insert(value):
    global hindex
    heap[hindex] = value # 루트노드 저장
    now = hindex
    hindex += 1
    while 1:
        p = now // 2 # 부모인덱스 구하기
        if p == 0: break # 해당노드가 루트노드라면 그냥 off
        if heap[p] >= heap[now]: break # 부모가 크거나 같으면 끄기 (maxheap 구현중)
        heap[p], heap[now] = heap[now], heap[p] # 부모가 더 작으면 자식이랑 swap
        now = p # swap당한 부모가 그 다음 프로세스의 자식이 되면서 위로 올라감....

def top():
    return heap[1]

def pop():
    global hindex
    hindex -= 1
    heap[1] = heap[hindex] # heap 1번 인덱스에 heap의 마지막 인덱스의 값을 올려줌
    heap[hindex] = 0
    now = 1
    while 1:
        son = now*2
        rson = now*2+1
        if rson<hindex and heap[son]<heap[rson]:
            son = rson # 오른쪽 자식이 있는데 and 왼보다 오른쪽이 크다 -> 앞으로 부모와 비교할 자식은 오른쪽 자식
        if son >= hindex or heap[now] > heap[son]:
            break # 자식이 없거나 or 부모가 자식보다 크다면 break
        heap[now], heap[son] = heap[son], heap[now]
        now = son





# insert 함수 완전이진트리로 저장
# top() 루트노드를 리턴하는 함수
# pop() 루트노드 출력 후 맨 뒤의 값을 맨 앞으로 올리고, 자식들이랑 비교 후 swap

for i in arr2:
    insert(i)

for i in range(len(arr2)):
    print(top(), end=" ")
    pop()