# import sys
# sys.stdin = open("input.txt","r")

arr = [list(map(int,input())) for _ in range(3)]

lst = []
for i in range(3):
    lst.append(len(arr[i]))

a,b,c = lst[0],lst[1],lst[2]

if a > b and a > c:
    for i in range(a):
        print(arr[0][i],end='')
elif b > a and b > c:
    for i in range(b):
        print(arr[1][i],end='')
elif c > a and c > a:
    for i in range(c):
        print(arr[2][i],end='')
elif a == b and a > c:
    index = 0
    while True:
        if arr[0][index] == arr[1][index]:
            index += 1
        else:
            if arr[0][index] > arr[1][index]:
                for i in range(a):
                    print(arr[0][i], end='')
                break
            else:
                for i in range(b):
                    print(arr[1][i], end='')
                break
elif a == c and a > b:
    index = 0
    while True:
        if arr[0][index] == arr[2][index]:
            index += 1
        else:
            if arr[0][index] > arr[2][index]:
                for i in range(a):
                    print(arr[0][i], end='')
                break
            else:
                for i in range(c):
                    print(arr[2][i], end='')
                break
elif b == c and b > a:
    index = 0
    while True:
        if arr[1][index] == arr[2][index]:
            index += 1
        else:
            if arr[1][index] > arr[2][index]:
                for i in range(b):
                    print(arr[1][i], end='')
                break
            else:
                for i in range(c):
                    print(arr[2][i], end='')
                break
elif a == b == c:
    tmp = []
    for i in range(3):
        cnt = 0
        while arr[i][cnt] == 1:
            cnt += 1
        tmp.append(cnt)

    tt = tmp.index(max(tmp))
    for i in range(lst[tt]):
        print(arr[tt][i],end='')