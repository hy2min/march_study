arr = [3,5,4,2]

lst = [i for i in map(int,input().split())]

for i in range(len(lst)):
    if lst[i] == 0:
        arr[i] = 0

ans = sum(arr)
print(ans)