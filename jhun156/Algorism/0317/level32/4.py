# import sys
# sys.stdin = open("input.txt","r")

arr = [list(input()) for _ in range(5)]
a, b = map(int,input().split())

arr[a].sort(key = lambda x: int(x))
arr[b].sort(key = lambda x: int(x))
for i in range(5):
    print(arr[i][0],end=' ')