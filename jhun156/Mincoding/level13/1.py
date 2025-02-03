def main():
    A,B = getName()
    if ord(A) > ord(B):
        print(B)
    else:
        print(A)

def getName():

    a,b = input().split()
    return a,b

main()