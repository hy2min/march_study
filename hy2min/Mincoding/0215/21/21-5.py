arr = [input() for _ in range(3)]
longeset_idx = max(range(len(arr)), key=lambda i: len(arr[i]))

arr[0], arr[longeset_idx] = arr[longeset_idx], arr[0]

def abc(arr, idx):
    if idx == len(arr):
        return
    print(arr[idx])
    abc(arr, idx+1)

abc(arr,0)