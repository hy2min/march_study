def gbb(st,ed):
    if st==ed:
        return st
    if ed-st == 1:
        return winer(st,ed)
    else:
        a=gbb(st,(st+ed)//2)
        b=gbb(((st+ed)//2)+1,ed)
        return winer(a,b)

def winer(i,j):
    ret = lst[i] - lst[j]
    if ret == 0:
        return i
    elif ret == 1:
        return i
    elif ret == -2:
        return i
    elif ret == -1:
        return j
    elif ret == 2:
        return j


T=int(input())

for tc in range(1,T+1):
    N=int(input())
    lst=list(map(int,input().split()))
    lst.insert(0,0)
    result = gbb(1,N)
    print(f'#{tc} {result}')
