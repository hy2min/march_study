# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
arr = []
for i in range(N):
    tmp = list(input().split())
    for j in range(i):
        if int(tmp[1]) >= int(arr[j][1]):
            arr.insert(j,tmp)
            break
    if len(arr) == i:
        arr.append(tmp)

    if len(arr) <= 2:
        for k in range(len(arr)):
            print(arr[k][0],end=' ')
        print()

    else:
        for k in range(3):
            print(arr[k][0],end=' ')
        print()