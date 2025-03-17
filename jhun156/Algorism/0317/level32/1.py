# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
arr = []
for _ in range(N):
    arr.append((input().split()))

arr.sort()
for i in arr:
    print(' '.join(i))