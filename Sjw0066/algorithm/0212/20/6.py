def abc(level):

    if level == b:
        print(level, end=" ")
        return
    print(level, end=" ")
    abc(level + 1)
    print(level, end=" ")


a,b=map(int,input().split())
abc(a)