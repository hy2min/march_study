from collections import Counter

n, person = map(int, input().split())
arr = [list(input().split()) for _ in range(person)]
count = Counter()
for i in range(person):
    arr[i][0] = int(arr[i][0])
    count[arr[i][0]] += 1

arr.sort(key=lambda x: -count[x[0]])

for i in range(person):
    if arr[i][0] == arr[0][0]:
        print(arr[i][1], end=" ")