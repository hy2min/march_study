a,b = map(int,input().split())

arr1 = [a for i in range(5)]
arr2 = [b for i in range(5)]

def PrintAll():
    global arr1,arr2
    for i in arr1:
        print(i,end='')
    print()
    for i in arr2:
        print(i,end='')

PrintAll()