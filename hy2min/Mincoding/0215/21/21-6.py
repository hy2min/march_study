branch, level = map(int, input().split())
cnt = 0
def abc(n):
    global cnt
    cnt += 1
    if n == level:
        return
    for i in range(branch):
        abc(n+1)
    
abc(0)
print(cnt)    