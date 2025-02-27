string = input()

def BBQ(level):
    for i in range(level):
        print(string[i], end = '')
    print()
    
    if level == len(string):
        return

    BBQ(level + 1)

BBQ(1)