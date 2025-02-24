N = int(input())
if N % 5 == 0:
    print(N//5)
else:
    a = N//5
    b = N%5
    if b == 3:
        print(a+1)
    elif a >= 1:
        a -= 1
        b += 5
        if b % 3 == 0:
            print(a+b//3)
        elif a >= 1:
            a -= 1
            b += 5
            if b % 3 == 0:
                print(a+b//3)
            else:
                print(-1)
        else:
            print(-1)
    else:
        print(-1)