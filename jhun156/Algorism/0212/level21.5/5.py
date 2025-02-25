# n = 8
arr = list(map(int,input().split()))

target = [0] * 10

for i in range(8):
    target[arr[i]] += 1

for i in range(1,10):
    target[i] += target[i-1]

lst = [0] * 8
for i in range(8):
    target[arr[i]] -= 1
    index = target[arr[i]]
    lst[index] = arr[i]

print(*lst)