arr = [
    [1,3,3,5,1],
    [3,6,2,4,2],
    [1,9,2,6,5],
]
n = int(input())
num_cnt = [0] * 10

for nums in arr:
    for num in nums:
        num_cnt[num] += 1

for i in range(1,10):
    if num_cnt[i] == n:
        print(i, end=" ")