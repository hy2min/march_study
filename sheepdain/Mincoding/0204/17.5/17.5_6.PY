password=[3,7,4,9]
n=list(map(int,input().split()))

def isSame(arr):
    if arr==password:
        return 'pass'
    else:
        return 'fail'

print(isSame(n))