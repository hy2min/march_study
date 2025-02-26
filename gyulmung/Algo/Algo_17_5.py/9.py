arr = [1, 0, 1, 0, 1, 0]

input_lst = list(map(int, input().split()))


Min_num = 1e8
for i in range(len(arr)):
    if arr[i] == 1:
        if Min_num > input_lst[i]:
            Min_num = input_lst[i]
            Min_y = i
print(f'arr[{Min_y}]={Min_num}')