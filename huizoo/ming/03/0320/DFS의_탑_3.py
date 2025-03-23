# 크리스마스 트리
import sys
input = sys.stdin.readline

def preorder(x):
    if x <= N:
        left, right = arr[x]
        print(x, end=' ')
        if left != -1:
            preorder(left)
        if right != -1:
            preorder(right)

def inorder(x):
    if x <= N:
        left, right = arr[x]
        if left != -1:
            inorder(left)
        print(x, end=' ')
        if right != -1:
            inorder(right)

def postorder(x):
    if x <= N:
        left, right = arr[x]
        if left != -1:
            postorder(left)
        if right != -1:
            postorder(right)
        print(x, end=' ')

N = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(N):
    idx, *children = map(int, input().split())
    arr[idx] = children

inorder(1)
print()
preorder(1)
print()
postorder(1)
