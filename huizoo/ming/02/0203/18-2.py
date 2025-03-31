arr = [list(map(int, input().split())) for _ in range(3)]
dat = [0] * 10

for row in arr : 
    for num in row : 
        dat[num] += 1

not_exist = [i for i in range(10) if not dat[i] and i != 0]
# dat = [0, 2, 2, 1, 1, 2, 0, 0, 0, 1]
print(*not_exist)