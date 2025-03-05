arr = [12,9,3,6]
a = int(input())
n = a//90

for i in range(n):
    arr.append(arr.pop(0))
    arr.append(arr.pop(1))

print(*arr)