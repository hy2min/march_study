arr = [5, 9, 4, 6, 1, 5, 8, 9]

idx, target = map(int, input().split())

sep_arr = arr[idx:]
result = sep_arr.index(target)

print(result)