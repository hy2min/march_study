arr = [
    [4,5,6,1,3,1],
    [2,1,3,6,3,6]
    ]


def input1() :
    a,b,c = map(int,input().split())
    return a,b,c


def process(a,b,c) :
    a1, b1, c1 = 0, 0, 0

    for i in range(2) :
        a1 += arr[i].count(a)
    for i in range(2) :
        b1 += arr[i].count(b)
    for i in range(2) :
        c1 += arr[i].count(c)

    return a1, b1, c1

def output(a,b,c,a1,b1,c1) :
    print(f"{a}={a1}개")
    print(f"{b}={b1}개")
    print(f"{c}={c1}개")

def main() :
    a,b,c = input1()
    a1, b1, c1 = process(a,b,c)
    output(a,b,c,a1,b1,c1)


main()