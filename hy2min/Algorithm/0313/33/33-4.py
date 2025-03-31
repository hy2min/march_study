arr = [0] * 10

def findboss(member):
    if isinstance(arr[member], str):  # 루트가 문자열이면 그대로 반환
        return arr[member]

    if arr[member] == member:
        return member

    ret = findboss(arr[member])
    arr[member] = ret
    return ret



def union(a, b):
    bossa, bossb = findboss(a), findboss(b)
    if findboss(a) == findboss(b):
        return
    if isinstance(bossa, int):
        arr[bossa] = bossb
    if isinstance(bossb, int):
        arr[bossb] = bossa
    else:
        arr[bossb] = bossa


n, k = map(int, input().split())

for _ in range(n):
    a, b = input().split()
    # if a.isdigit() and b.isdigit():
    #     union(int(a), int(b))
    # else:
    if a.isdigit():
        a = int(a)

    if b.isdigit():
        b = int(b)

    union(a, b)

for i in range(1, k+1):
    print(arr[i], end="")