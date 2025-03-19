N = int(input())
dat = [0]*200
arr = []
for _ in range(N):
    arr.append(input().split())

def findboss(m):
    if dat[ord(m)] == 0: return m
    ret=findboss(dat[ord(m)])
    dat[ord(m)]=ret
    return ret

def union(a, b):
    fa, fb = findboss(a), findboss(b)
    if fa == fb:
        return 1
    dat[ord(fb)] = fa

answer = 0
for i in range(N):
    a, b = arr[i]
    ret = union(a, b)
    if ret:
        answer = 1
        break
if answer:
    print('발견')
else: print('미발견')