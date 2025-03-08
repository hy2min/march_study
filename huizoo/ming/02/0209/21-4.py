level = int(input())
def fun(a, n=2) : 
    print(level-a, end='')
    if a > 0 : 
        for _ in range(n) : 
            fun(a-1)

fun(level)