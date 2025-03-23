n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr2 = [list(map(int, input().split())) for _ in range(n)]
arr3 = []
for i in range(n):
    for j in range(n):
        if arr2[i][j]:
            arr3.append(arr[i][j])
freq = {}
for num in arr3:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

arr3.sort(key=lambda x: (-freq[x], x))
print(*arr3)