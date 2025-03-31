arr = [input() for _ in range(3)]

print(max(arr, key=lambda x: (len(x), x)))