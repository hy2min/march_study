arr = [0] * 26
def find_boss(member):
    if arr[ord(member)-65] == 0:
        return member
    ret = find_boss(arr[ord(member)-65])
    arr[ord(member)-65] = ret
    return ret

def union(a, b):
    bossa, bossb = find_boss(a), find_boss(b)
    if bossa == bossb:
        return
    arr[ord(bossb)-65] = bossa




# alliance : union
# war : population 비교 후 큰 쪽으로 흡수

n = int(input())
population = list(map(int, input().split()))
case = int(input())
for _ in range(case):
    action, a, b = input().split()
    if action == 'alliance':
        union(a, b)
    # elif action == 'war':
    #     absorb(a, b)

print(arr)