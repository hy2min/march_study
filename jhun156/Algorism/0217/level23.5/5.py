# import sys
# sys.stdin = open("input.txt","r")

lst = list(map(int,input().split()))
n = len(lst)
pivot = lst[0]
st,ed = 0,n-1
while 1:
    for i in range(st,n):
        if lst[i] > pivot:
            st = i
            break
    for i in range(ed,-1,-1):
        if lst[i] < pivot:
            ed = i
            break
    if st > ed:
        break
    else:
        lst[st], lst[ed] = lst[ed], lst[st]

lst[ed],lst[0] = lst[0],lst[ed]
print(*lst)