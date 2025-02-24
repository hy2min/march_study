arr = list(map(int, input().split()))
def jack(i):
    print(arr[i], end=' ')
    if i == len(arr)-1:
        return
    jack(i+1)
    print(arr[i], end=' ')
jack(0)