arr = [
    [3,5,9],
    [4,2,1],
    [5,1,5],
]
nums = list(map(int, input().split()))

for i in range(3):
    flag = 0
    for j in range(3):
        if nums[i] in arr[j]:
            flag = 1
    if not flag:
        print(f'{nums[i]}:미발견')
    else:
        print(f'{nums[i]}:존재')