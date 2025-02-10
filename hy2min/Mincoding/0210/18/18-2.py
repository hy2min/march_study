arr = []
for _ in range(3):
    arr.append(list(map(int, input().split())))
arr_t = [0] * 10
for nums in arr:
    for num in nums:
        arr_t[num] += 1

for i in range(1,10):
    if arr_t[i] == 0:
        print(i, end=" ")
