string = list(input())

def BBQ(level):
    
    if level == len(string):
        return
    
    BBQ(level + 1)

    for i in range(1):
        for j in range(level, len(string)):
            print(string[j], end = '')
        print()

BBQ(0)