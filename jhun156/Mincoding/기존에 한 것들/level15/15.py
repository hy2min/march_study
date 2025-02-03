arr = [[0] * 8 for _ in range(2)]
a = list(input())
b = list(input())
lst = [a,b]

for i in range(2):
    for j in range(len(lst[i])):
        arr[i][j] = lst[i][j]
count = 0
for j in range(8):
    if arr[0][j] != arr[1][j]:
        count += 1

print(count)