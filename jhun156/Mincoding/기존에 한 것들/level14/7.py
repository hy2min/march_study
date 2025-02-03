arr = [i for i in map(int,input().split())]

arr.sort(reverse=True)

for i in arr:
    print(i,end='')