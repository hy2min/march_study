num = int(input())

def bbq(level):

    if level == 0:
        return
    
    bbq(level//2)
    print(level, end = ' ')



bbq(num)