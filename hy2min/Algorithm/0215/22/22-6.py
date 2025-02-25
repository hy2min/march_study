arr = [input() for _ in range(4)]
min_idx, max_idx = 0, 0


def abc(i):
    global max_idx, min_idx
    if i == len(arr):
        print(f'긴문장:{max_idx}')
        print(f'짧은문장:{min_idx}')
        return

    if len(arr[i]) > len(arr[max_idx]):
        max_idx = i
    if len(arr[i]) < len(arr[min_idx]):
        min_idx = i

    abc(i + 1)


abc(0)
