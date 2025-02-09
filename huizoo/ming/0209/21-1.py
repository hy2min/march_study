x, y = 2, 3
def one(a, b) : 
    if a > 0 :
        for _ in range(b) : 
            one(a-1, b)

one(2, 3)