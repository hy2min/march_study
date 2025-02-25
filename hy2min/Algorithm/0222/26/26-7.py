arr = [3,5,5,6,9,1,2]
s,e = map(int, input().split())

arr[s:e+1] = arr[s:e+1][::-1]

print(*arr)