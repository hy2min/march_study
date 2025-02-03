arr = [
    [3,1,6],
    [7,8,4],
    [9,2,3],
]

a,b,c = map(int,input().split())

arr[a][b] = c

MAX = max(map(max,arr))
MIN = min(map(min,arr))

print(MAX+MIN)