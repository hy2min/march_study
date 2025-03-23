arr = [5,9,4,6,1,5,8,9]
n, a = map(int, input().split())
Offset = arr[n:].index(a)
print(Offset)