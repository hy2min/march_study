arr = [input() for _ in range(3)]
max_idx = arr.index(max(arr, key=len))
arr[0], arr[max_idx] = arr[max_idx], arr[0]
print('\n'.join(arr))