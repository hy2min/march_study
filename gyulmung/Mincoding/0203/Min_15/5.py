arr = [[0]*6 for _ in range(4)]
for i in range(4):
    numbers = list(map(str, input().split()))
    arr.append(numbers)

num_arr = [0]*4


for i in range(4):
    count = 0
    for j in range(6):
        if arr[i][j] != 0:
            count += 1
        else:
            break
    num_arr[i] = count

print(*num_arr)