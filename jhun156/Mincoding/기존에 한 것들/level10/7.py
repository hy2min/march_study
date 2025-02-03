def GOP():
    
    a,b = map(int,input().split())
    return a * b

def SUM():

    a,b = map(int,input().split())
    return a + b

def main():

    gp = GOP()
    sm = SUM()

    if gp > sm:
        print("GOP>SUM")
    elif sm > gp:
        print("GOP<SUM")
    else:
        print("GOP==SUM")

main()
