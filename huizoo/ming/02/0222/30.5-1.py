K = int(input())
arr = [12, 9, 3, 6]
K = (K//90)%4
for i in range(K):
    arr = [arr[1], arr[3], arr[0], arr[2]]

print(*arr)