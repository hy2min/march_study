def abc(level):
    if level == 5:
        print()
        return
    print(lst[level],end="")
    abc(level + 1)
    print(lst[level],end="")


lst = list(input())
abc(0)
