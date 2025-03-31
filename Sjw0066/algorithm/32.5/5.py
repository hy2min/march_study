arr=[3,2,-1,3,2,0,-1]

st=int(input())

def trace(now):

    if now==5:
        print(f'{now}번')
        return

    trace(arr[now]+now)
    print(f'{now}번')

trace(st)