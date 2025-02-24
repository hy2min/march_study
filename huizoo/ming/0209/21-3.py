level = int(input())
branch = int(input())
def one(a, b) : 
    if a > 0 :
        for _ in range(b) : 
            one(a-1, b)

one(level, branch)