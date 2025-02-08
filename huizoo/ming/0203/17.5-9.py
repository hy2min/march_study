arr = list(map(int, input().split()))
mask = [1,0,1,0,1,0]
mask_arr = []
for i in range(6) : 
    if mask[i] : 
        mask_arr.append(arr[i])
min_arr = min(mask_arr)
print(f'arr[{arr.index(min_arr)}]={min_arr}')