import sys
sys.stdin=open('input.txt','r')

n = int(input())
arr = [[0]*3 for i in range(3)]
plant = []
for i in range(n):
    init = list(map(int, input().split()))
    plant.append(init)
for y, x, p in plant:
    arr[y][x] = list(str(p))

m = int(input())
wind = list(map(int, input().split()))
for i in range(m):
    for y,x,p in plant:
        if not arr[y][x]: continue
        if int(arr[y][x][-1]) - wind[i] <= 0:
            arr[y][x].pop()
        else:
            arr[y][x][-1] = int(arr[y][x][-1]) - wind[i]
Sum = 0
for y,x,p in plant:
    if not arr[y][x]: continue
    if arr[y][x][-1]:
        Sum+=len(arr[y][x])
print(Sum)