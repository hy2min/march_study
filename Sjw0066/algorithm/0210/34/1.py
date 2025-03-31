arr=[4,4,5,7,8,10,20,22,23,24]

def binary_search(st,ed,target):

    while 1:
        mid=(st+ed)//2

        if arr[mid]==target:
            return 1
        elif arr[mid]> target:
            ed = mid - 1
        elif arr[mid]<target:
            st = mid + 1
        if st>ed:
            return 0

flag=binary_search(0,len(arr),int(input()))

if flag :
    print('O')
else:
    print('X')