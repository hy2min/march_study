try:
    arr = [list(map(int, input().split()))for _ in range(2)]
    lst = []
    for i in arr:
        for j in i:
            lst.append(j)

    for i in range(5):
        for j in range(i+1, 6):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i]

    index = 0
    for i in range(2):
        for j in range(3):
            arr[i][j] = lst[index]
            index += 1

    for i in range(2):
        for j in range(3): 
            print(arr[i][j], end = ' ')
        print()


except IndexError:
    lst = list(map(int, input().split()))
    arr = [[0]*3 for _ in range(2)]

    for i in range(5):
        for j in range(i+1, 6):
            if lst[i] > lst[j]:
                lst[i],lst[j] = lst[j],lst[i]

    index = 0
    for i in range(2):
        for j in range(3):
            arr[i][j] = lst[index]
            index += 1

    for i in range(2):
        for j in range(3): 
            print(arr[i][j], end = ' ')
        print()
