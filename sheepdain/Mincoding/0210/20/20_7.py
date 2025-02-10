def abc(n):
    print(arr[n], end=' ')
    if n==0: return
    abc(n-1)
    print(arr[n], end=' ')

arr=[3,7,4,1,9,4,6,2]
a=int(input())
abc(a)