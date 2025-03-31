def abc(level):

    if level == 0:
        print(arr[level], end=" ")
        return
    print(arr[level], end=" ")
    abc(level - 1)
    print(arr[level], end=" ")


arr=[3,7,4,1,9,4,6,2]
index=int(input())
abc(index)
