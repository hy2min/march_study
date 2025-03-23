numbers = list(map(int, input().split()))

arr = [
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16],
]

dat = [0]*16
plus_num = 1
for i in range(16) : 
    for num in numbers : 
        if i == num-1 : 
            dat[i] += plus_num
            plus_num += 1

for i in range(0, 16, 4) : 
    print(*dat[i:i+4])
