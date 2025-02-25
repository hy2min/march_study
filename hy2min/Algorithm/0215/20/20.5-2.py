s = input()

def abc(level):
    print(s[-level:])
    if level == len(s):
        return
    abc(level+1)

abc(1)