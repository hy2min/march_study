from collections import Counter

n, person = map(int, input().split())
arr = [list(input().split()) for _ in range(person)]
for i in range(person):
    arr[i][0] = int(arr[i][0])

