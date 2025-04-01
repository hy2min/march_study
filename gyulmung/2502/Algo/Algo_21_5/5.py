numbers = list(map(int, input().split()))
arr = [0]*10
numbers_sort = [0]*len(numbers)

for i in range(len(numbers)):
    arr[numbers[i]] += 1
for i in range(1, len(arr)):
    arr[i] = arr[i - 1] + arr[i]
for i in range(len(numbers)):
    arr[numbers[i]] -= 1
    numbers_sort[arr[numbers[i]]] = numbers[i]


print(*numbers_sort)