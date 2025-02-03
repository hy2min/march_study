a=list(map(int,input().split()))
arr=[]
for i in range(0,6,3):
    arr.append(a[i:i+3])
def MAX(arr):
    n=max(a)
    for i in range(2):
        for j in range(3):
            if n==arr[i][j]:
                return print(f'({i},{j})')
def MIN(arr):
    n=min(a)
    for i in range(2):
        for j in range(3):
            if n==arr[i][j]:
                return print(f'({i},{j})')
MAX(arr)
MIN(arr)