def abc(n):
    print(arr[n],end='')
    if n==4:
        print()
        return print(arr[n],end='')
    abc(n+1)
    print(arr[n],end='')

arr=input()
abc(0)