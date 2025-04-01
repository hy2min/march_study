import sys
sys.stdin=open('input.txt','r')

n = int(input())
arr = [0,1,2,3,4,5,6,7,8,9]

def Plus(level, Sum):
    global cnt
    if level == n:
        if Sum == 7:
            cnt += 1
            return
        return

    for i in range(10):
        Plus(level+1, Sum+arr[i])

cnt = 0
Plus(0, 0)
print(cnt)