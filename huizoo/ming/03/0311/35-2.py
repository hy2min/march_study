n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = []
for i in range(n):
    for j in range(n):
        if arr[i][j]:
            arr2.append((arr[i][j], i, j))

length = len(arr2)
def abc(i, nn):
    big = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left <= nn - 1 and arr2[big][0] < arr2[left][0]:
        big = left
    if right <= nn - 1 and arr2[big][0] < arr2[right][0]:
        big = right
    if big != i:
        arr2[big], arr2[i] = arr2[i], arr2[big]
        abc(big, nn)

for i in range(length//2 - 1, -1, -1):
    abc(i, length)

for i in range(length-1, 0, -1):
    arr2[0], arr2[i] = arr2[i], arr2[0]
    abc(0, i)

for i in range(length-1, length-4, -1):
    print(f'{chr(arr2[i][1]+65)}-{chr(arr2[i][2]+65)} {arr2[i][0]}')