arr=[list(input()) for _ in range(3)]

max_index=0
max_len=0
for i in range(3):
    if max_len<len(arr[i]):
        max_len=len(arr[i])
        max_index=i

arr[0] , arr[max_index] = arr[max_index], arr[0]

for i in arr:
    print(''.join(i))