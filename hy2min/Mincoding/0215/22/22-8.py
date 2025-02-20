arr = [
    [[2,4],[1,5]],
    [[2,3],[3,6]],
    [[7,3],[1,5]],
]
def abc(arr):
    if isinstance(arr,int):
        return arr, arr

    min_n, max_n = 21e8, -21e8
    for i in arr:
        sub_min, sub_max = abc(i)
        min_n = min(sub_min, min_n)
        max_n = max(sub_max, max_n)

    return min_n, max_n

n = int(input())


print(f'MAX={abc(arr[n])[1]}')
print(f'MIN={abc(arr[n])[0]}')
