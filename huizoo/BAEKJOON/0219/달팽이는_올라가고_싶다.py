import sys
A, B, V = map(int, sys.stdin.readline().split())
if A >= V:
    print(1)
else:
    C = A-B
    if (V-A)%C == 0:
        print((V-A)//C+1)
    else:
        print((V-A)//C+2)
