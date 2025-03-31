# import sys
# sys.stdin = open("input.txt","r")

T, n = map(int,input().split())
arr = list(map(int,input().split()))
Min = 21e8
flag = 0

def find(level,money):

    global Min,flag

    if money < 0 or level > Min:
        return

    elif money == 0:
        Min = min(Min,level)
        flag = 1
        return

    for i in range(n):
        find(level+1,money-arr[i])

find(0,T)
if flag:
    print(Min)
else:
    print("impossible")