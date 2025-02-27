lst=list(map(int,input().split()))

pivot=lst[0]

def sort(st,ed):



    for i in range(st,len(lst)):
        if lst[i]>pivot:
            a=i
            break

    for i in range(ed,-1,-1):
        if lst[i]<pivot:
            b=i
            break

    if a>b:
        lst[0] , lst[b] = lst[b],lst[0]
        return

    lst[a],lst[b] = lst[b],lst[a]

    sort(a,b)

sort(0,len(lst)-1)

print(*lst)

