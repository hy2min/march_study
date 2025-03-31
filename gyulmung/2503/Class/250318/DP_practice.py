import sys
sys.stdin = open('input.txt', 'r')

n, m = map(int, input().split())
arr = [(0,0)]
for i in range(n):
    w, v = map(int, input().split())
    arr.append((w, v))
print(arr)
lst = [[0]*(m+1) for _ in range(n+1)]
print(lst)

for i in range(1, n+1):
    for j in range(1, n+1):
        weight = arr[i][0]
        value = arr[i][1]

