arr = [0]*10
def find_boss(n):
    if arr[n] == 0:
        return n
    ret = find_boss(arr[n])
    arr[n] = ret
    return ret

def union(a, b):
    boss_a, boss_b = find_boss(a), find_boss(b)

    if boss_a == boss_b:
        return False

    if boss_a.isdigit() and boss_b.isdigit():
        arr[boss_b] = boss_a
    elif boss_a.isalpha():
        arr[boss_b] = boss_a
    elif boss_b.isalpha():
        arr[boss_a] = boss_b

    return True

n, k = map(int, input().split())
for _ in range(n):
    a, b = input().split()
    a = int(a) if a.isdigit() else a
    b = int(b) if b.isdigit() else b
    union(a, b)
