number = int(input())
arr = [0]*5
result = [[]]
for i in range(5):
    shrimp = list(map(int, input().split()))
    arr[i] = shrimp
print(arr)
for i in range(5):
    if number == 1:
        for j in range(i+1):
            print(arr[i][j], end = ' ')
    elif number == 2:
        for j in range(5-i):
            print(arr[i][j], end = ' ')
    print()