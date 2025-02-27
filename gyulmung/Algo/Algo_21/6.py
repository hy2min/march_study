branch, level = map(int, input().split())
cnt = 0

def abd(lev):
    global cnt
    cnt += 1
    if lev == level:
        return
    for i in range(branch):
        abd(lev + 1)

abd(0)
print(cnt)