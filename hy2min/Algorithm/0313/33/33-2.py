arr = [0] * 10  # a~j 까지

def find_boss(m):
    if arr[ord(m)-65] == 0:
        return m
    ret = find_boss(arr[ord(m)-65])
    arr[ord(m)-65] = ret
    return ret

def union(a, b):
    global arr
    boss_a, boss_b = find_boss(a), find_boss(b)
    if boss_a == boss_b:
        return
    arr[ord(boss_b)-65] = boss_a

n = int(input())
for _ in range(n):
    a, b = input().split()
    union(a, b)

ans = set(arr)
if 0 not in ans:
    print(f'{len(ans)}개')
else:
    print(f'{len(ans)-1}개')