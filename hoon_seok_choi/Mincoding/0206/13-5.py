
def main() :
    c1,c2 = KFC()
    print(f"대문자{c1}개\n소문자{c2}개")


def KFC() :
    a = input()

    arr = [*a]
    cnt_1 = 0
    cnt_2 = 0

    # print(arr)
    for i in arr :
        if i.isupper() :
            cnt_1 +=1
        elif i.islower() :
            cnt_2 +=1
    
    return cnt_1, cnt_2

main()