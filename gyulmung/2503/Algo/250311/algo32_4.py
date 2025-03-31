import sys
sys.stdin=open('input.txt','r')

arr = [list(input()) for _ in range(5)]
n, m = map(int, input().split())
arr[n] = sorted(arr[n], key=lambda x:x)
arr[m] = sorted(arr[m], key=lambda x:x)
for i in range(5):
    print(arr[i][0], end = ' ')