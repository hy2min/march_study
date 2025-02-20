arr = [
    [[2,4],[1,5]],
    [[2,3],[3,6]],
    [[7,3],[1,5]],
]

def abc(arr):
    if isinstance(arr,int):
        return arr, arr

    max_n, min_n = -21e8, 21e8

    for i in arr:
        sub_min, sub_max = abc(i)
        max_n = max(max_n,sub_max)
        min_n = min(min_n,sub_min)
    return min_n, max_n


n = int(input())

print(f'MAX={abc(arr[n])[1]}')
print(f'MIN={abc(arr[n])[0]}')
