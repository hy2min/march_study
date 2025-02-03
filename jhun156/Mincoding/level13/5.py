def main():
    da,so = KFC()
    print(f"대문자{da}개\n소문자{so}개")

def KFC():
    lst = list(input())
    Dcount,Scount = 0,0
    for i in lst:
        if i.isupper():
            Dcount += 1
        else:
            Scount += 1
    return Dcount,Scount

main()