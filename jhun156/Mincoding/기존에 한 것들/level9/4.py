arr = [3,4,2,5,7,9]

a,b = map(int,input().split())

tmp = arr[a]
arr[a] = arr[b]
arr[b] = tmp

print(*arr)