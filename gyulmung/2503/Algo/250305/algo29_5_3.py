arr = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    lst = []
    for j in range(3):
        if not lst:
            lst.append(arr[i].pop(0))
        if not arr[i]:
            print(lst[-1])
            break
        if lst[-1] == arr[i][0]:
            lst.append(arr[i].pop(0))
        else:
            print('x')
            break
