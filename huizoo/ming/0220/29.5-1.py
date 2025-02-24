def jump(x):
    if x == len(arr)-1:
        print(arr[x],end=' ')
        return
    print(arr[x],end=' ')
    jump(x+arr[x])
    print(arr[x],end=' ')

n = int(input())
arr = ['시작',3,1,2,1,3,2,1,2,1,'도착']

print('시작', end=' ')
jump(n)
print('시작', end=' ')
