import heapq

inf = 21e8

arr = [
    [0,5,inf,8],
    [7,0,9,inf],
    [2,inf,0,4],
    [inf,inf,3,0],
]

for ky in range(4):
    for start in range(4):
        for end in range(4):
            if arr[start][end] > arr[start][ky] + arr[ky][end]:
                arr[start][end] = arr[start][ky] + arr[ky][end]

for i in arr:
    print(*i)