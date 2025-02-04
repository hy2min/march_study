
def getName() :
    name1, name2 = map(str, input().split())
    return name1, name2

def main(name1, name2) :
    # a = list(name1)[0]
    # b = list(name2)[0]

    if ord(name1) < ord(name2) :
        print(name1)
    else :
        print(name2)


a,b = getName()
main(a,b)
