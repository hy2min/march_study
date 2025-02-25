n = int(input())
arr = [input() for _ in range(n)]
target = "CHRISTMAS"
cnt = 0

# level = 4, branch = n
def abc(level, s):
    global cnt
    used = [0] * n
    if level == 4:
        if s == target:
            cnt += 1
        return
    for i in range(n):
        if not used[i]:
            used[i] = 1
            abc(level + 1, s + arr[i])
            used[i] = 0

abc(0,"")
print(cnt)