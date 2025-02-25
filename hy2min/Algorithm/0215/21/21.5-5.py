vect = list(map(int, input().split()))
bucket = [0] * 10
arr = [""] * len(vect)
for i in vect:
    bucket[i] += 1

for i in range(1, 10):
    bucket[i] += bucket[i-1]

for i in range(len(vect)-1, -1, -1):
    bucket[vect[i]] -= 1
    arr[bucket[vect[i]]] = vect[i]

print(*arr)

