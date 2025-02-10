N=int(input())
data=[list(map(str,input())) for _ in range(N)]


def binary_search_row(st,ed):
    Max=-1

    while 1:
        mid=(st+ed)//2

        if data[mid][0]!='#':
            ed=mid-1                      
        else: 
            Max=mid
            st=mid+1

        if st>ed:
            break
    return Max+1

def binary_search_col(st,ed,y):
    Max=-1

    while 1:
        mid=(st+ed)//2
        if data[y][mid] !='#':
            ed=mid-1
                       
        else: 
            Max=mid
            st=mid+1

        if st>ed:
            break
    return Max+1

y=binary_search_row(0,N-1)
y-=1
x=binary_search_col(0,N-1,y)
print(y,x)