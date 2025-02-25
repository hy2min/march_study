


def main() :
    a,b = map(int, input().split())
    sum, gop = ABC(a,b)
    print(sum, gop)


def ABC(a,b) :
    sum = a + b
    gop = a * b
    return sum, gop

main()


