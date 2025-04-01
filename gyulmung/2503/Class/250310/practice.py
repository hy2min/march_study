arr=[0]*200
def findboss(member):
    global arr
    if arr[ord(member)] == 0:
        return member
    ret = findboss(arr[ord(member)])
    return ret

def union(a,b):
    global arr
    bossA, bossB = findboss(a), findboss(b)
    if bossA == bossB:
        return
    arr[ord(bossB)] = bossA

union('A', 'B')
union('D', 'E')
union('B', 'E')
union('B', 'D')
union('E', 'F')

y, x = input().split()
if findboss(y) == findboss(x):
    print('같은 그룹')
else: print('다른 그룹')