arr = [3, 7, 4, 1, 9, 4, 6, 2]
Index = int(input())

def bbq(level):

    print(arr[level], end = " ")

    if level == 0:
        return

    bbq(level - 1)
    print(arr[level], end = ' ')


bbq(Index)