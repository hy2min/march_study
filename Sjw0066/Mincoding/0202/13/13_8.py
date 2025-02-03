
def main():
    arr1=[3,5,1,2,7]
    arr2=list(map(int,input().split()))
    
    result=CompareGo(arr1,arr2)
    print(result)
    
    

def CompareGo(arr1,arr2):
    cnt=0
    for i in range(len(arr1)):
        if arr1[i] == arr2[i]:
            cnt+=1

    if cnt == 5 :
        return "두배열은완전같음"
    else:
        return "두배열은같지않음"

main()