def union(a,b):
    global arr,flag

    bossA,bossB=findboss(a),findboss(b)

    if bossA==bossB:
        flag=1
        return

    arr[ord(bossB)]=bossA

def findboss(member):

    if arr[ord(member)] == 0:
        return member

    ret = findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return ret

N=int(input())
flag=0
arr=[0]*100
for _ in range(N):
    a1,b1=input().split()
    union(a1,b1)

if flag:
    print('발견')
else:
    print('미발견')