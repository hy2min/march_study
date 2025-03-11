arr = [list(input()) for _ in range(5)]
arr = [[int(j) for j in i] for i in arr]
line1, line2 = map(int, input().split())
arr[line1].sort()
arr[line2].sort()

for i in range(5):
    print(arr[i][0], end=" ")