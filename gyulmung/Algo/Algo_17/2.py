arr = [5, 9, 4, 6, 1, 5, 8, 9]

Index, target = map(int, input().split())

for i in range(Index,len(arr)):
    if target == arr[i]:
        print(i - Index)