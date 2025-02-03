a,b = 0,0

def mincoding(A,B):
    A,B = map(int,input().split())
    return A,B

def main(c,d):
    c,d = mincoding(c,d)
    print(f"({c})({d})")

main(a,b)