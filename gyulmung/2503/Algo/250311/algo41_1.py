import sys
sys.stdin = open('input.txt', 'r')

def Su(level):
    global lst
    lst[level] = lst[level -1] + lst[level -2]

    if level == idx:
        print(lst[level])
        return
    Su(level + 1)


n = int(input())
idx = n-1
lst = [0]*(n+1)
lst[0] = 0
lst[1] = 1

if idx == 0:
    print(lst[0])
elif idx == 1:
    print(lst[1])
else:
    Su(2)