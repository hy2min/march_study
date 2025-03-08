arr = [3,7,4,1,9,4,6,2]
idx = int(input())
def abc(i):
    print(arr[i], end = ' ')
    if i == 0:
        return
    abc(i-1)
    print(arr[i], end=' ')
abc(idx)