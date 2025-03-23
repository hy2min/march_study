arr = [
    ['A', 'B', 'C'],
    ['D', 'E', 'F'],
    ['G', 'H'],
    ['I', 'J'],
]
n = int(input())
for _ in range(n):
    a, b = input().split()
    idx1, idx2 = -1, -1
    for i in range(len(arr)):
        if a in arr[i]:
            idx1 = i
        if b in arr[i]:
            idx2 = i
    if idx1 == idx2: continue
    temp = arr.pop(idx2)
    arr[idx1] += temp

print(f'{len(arr)}개')