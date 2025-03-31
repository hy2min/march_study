

def main() :

    arr = [3,5,1,2,7]

    arr2 = list(map(int,input().split()))

    compareGo(arr, arr2)


def compareGo(a,b) :
    cnt = 0
    for i in range(len(a)) :
        if a[i] == b[i] :
            pass
        else :
            cnt +=1

    if cnt == 0 :
        print("두배열은완전같음")
    elif cnt >= 1 :
        print("두배열은같지않음")
    
main()