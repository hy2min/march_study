arr = [list(input()) for _ in range(5)]
len_arr=[]

len_index=0
max_len=0

for i in range(len(arr)):
    if max_len<len(arr[i]):
        max_len=len(arr[i])
        len_index=i



print(''.join(arr[len_index]))