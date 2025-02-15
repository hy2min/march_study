vect = 'MINCODING'
n = int(input())    
arr = list(input().split())
for i in range(n):
    if arr[i] in vect:
        print('o', end='')
    else :
        print('x', end='')