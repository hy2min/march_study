lst = list(map(int, input().split()))

def BBQ(level):
    for i in range(0, 4 + level):
        print(lst[i], end = " ")
    print()
    if level == 3:
        return
    
    BBQ(level + 1)

BBQ(0)