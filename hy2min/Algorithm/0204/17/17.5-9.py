arr = list(map(int, input().split()))
masking_arr = [1,0,1,0,1,0]
arr_dict = {}
for i in range(6):
    if masking_arr[i]:
        arr_dict[i] = arr[i]
for i in list(arr_dict.keys()):
    if arr_dict[i] == min(arr_dict.values()):
        print(f'arr[{i}]={arr_dict[i]}')
        break