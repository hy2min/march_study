a, b = map(int, input().split())
cnt = 0
def fun(branch, level) : 
    global cnt
    cnt += 1
    if level > 0 : 
        for _ in range(branch) : 
            fun(branch, level-1)

fun(a, b)

print(cnt)