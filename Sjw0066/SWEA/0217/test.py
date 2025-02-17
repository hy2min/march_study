T=int(input())

def flip_stone(a,b):

    for i in range(1,b+1):
        right=a+i-1
        left= a-i-1
        if left<0 or right>N-1:
            continue
        if arr[right] == arr[left]:
            arr[left] = 1-arr[left]
            arr[right] = 1-arr[right]

for tc in range(1,T+1):
    N,M = map(int,input().split())
    arr=list(map(int,input().split()))

    for i in range(M):
        a,b=map(int,input().split())
        flip_stone(a,b)


    print(f'#{tc}',end=" ")
    for i in arr:
        print(i,end=" ")
    print()