def main():
    lst1 = [3,5,1,2,7]
    lst2 = [i for i in map(int,input().split())]
    CompareGo(lst1,lst2)

def CompareGo(arr1,arr2):
    if arr1 == arr2:
        print("두배열은완전같음")
    else:
        print("두배열은같지않음")

main()