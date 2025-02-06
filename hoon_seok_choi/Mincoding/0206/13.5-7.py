arr = [
    ['D', 'A', 'S'],
    ['Q', 'W', 'V'],
    ['R', 'T', 'Y']
]

def main() :
    a,b = map(int,input().split())
    c,d = map(int,input().split())

    a1, b1 = Find(a,b,c,d)
    print(a1,b1)


def Find(a,b,c,d) :
    a1 = arr[a][b]
    b1 = arr[c][d]

    return a1, b1

main()