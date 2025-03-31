arr = [0]*3
for i in range(3):
    numbers = list(map(int, input().split()))
    arr[i] = numbers

numbers_sum = 0

for i in range(3):
    for j in range(i + 1):
        numbers_sum += arr[i][j]
print(numbers_sum)