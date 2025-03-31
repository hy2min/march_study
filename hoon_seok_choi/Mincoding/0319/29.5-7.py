import copy

a,b = map(int,input().split())

arr =['_']*5
arr[a]=b

while 1:
    arr2 = copy.deepcopy(arr)

    if 0 in arr2:
        arr2[arr2.index(0)] = '_'
        for i in arr2:
            print(i,end='')
        print()
        break

    for i in arr:
        print(i,end='')
    print()

    
    for i in range(5):
        if arr2[i]!='_' and arr2[i] != 0:
            arr[i+1] = arr[i] -1
            arr[i] = '_'

        







