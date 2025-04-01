import sys
sys.stdin = open('input.txt','r')

n = int(input())
lst = [0]*101
arr = [list(input().split()) for _ in range(n)]
print(arr)

for i in range(n):
    lst[int(arr[i][1])] = arr[i][0]
print(lst)