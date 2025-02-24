arr = list(map(int, input().split()))
mask = [1, 0, 1, 0, 1, 0]
for i in range(6):
    if mask[i]:
        pass
    else:
        arr[i] = 21e8
print(f'arr[{arr.index(min(arr))}]={min(arr)}')