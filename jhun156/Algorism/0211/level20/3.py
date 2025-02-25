arr = list(map(int,input().split()))

def step(num):

    print(arr[num],end=' ')
    if num == 5:
        return

    step(num+1)
    print(arr[num],end=' ')

step(0)