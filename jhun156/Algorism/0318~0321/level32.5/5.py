idx = int(input())
arr = [
    [3, '>>'],
    [2, '>>'],
    [1, '<<'],
    [3, '>>'],
    [2, '<<'],
    ['테러범', '테러범'],
    [1, '<<'],
]

def track(index):

    if arr[index][1] == '테러범':
        print(f"{index}번")
        return

    if arr[index][1] == '>>':
        track(index+arr[index][0])
        print(f"{index}번")
    else:
        track(index-arr[index][0])
        print(f"{index}번")


track(idx)