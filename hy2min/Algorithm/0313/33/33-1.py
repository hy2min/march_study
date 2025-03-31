arr = [0] * 200

def findboss(n):
    if arr[ord(n)] == 0:
        return n
    ret = findboss(arr[ord(n)])
    arr[ord(n)] = ret
    return ret
def union(a, b):
    global arr
    boss_a, boss_b =findboss(a), findboss(b)
    if boss_a == boss_b:
        return False
    arr[ord(boss_b)] = boss_a
    return True
n = int(input())
ans = False
for _ in range(n):
    a,b = input().split()
    ret = union(a,b)
    if not ret:
        ans = True

if ans:
    print('발견')
else:
    print('미발견')