def BBQ():
    lst = list(map(int, input().split()))
    Max = -1e8
    Min = 1e8
    for i in range(len(lst)):
        if Max < lst[i]:
            Max = lst[i]
        if Min > lst[i]:
            Min = lst[i]
    return Max, Min

a, b = BBQ()
print(f'a={a}\nb={b}')