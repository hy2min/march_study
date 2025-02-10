def Movement(n):
    print(arr[n], end=' ')
    if n==len(arr)-1: return
    Movement(n+1)
    print(arr[n], end=' ')

arr=list(map(int,input().split()))
Movement(0)