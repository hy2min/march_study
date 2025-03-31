n = int(input())
lst = [''] * n
for i in range(n):
    name, score = input().split()
    score = int(score)
    lst[i] = [name, score]

arr = [lst[0][0]]
print(*arr)
for i in range(1,n):
    arr.append(lst[i][0])
    for j in range(i, 0, -1):
        if lst[j-1][1] <= lst[j][1]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            lst[j-1], lst[j] = lst[j], lst[j-1]
    print(*arr[:3])

