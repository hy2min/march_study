T= int(input())

for tc in range(1, T + 1):
    test_case,N=map(str,input().split())
    N=int(N)

    arr=list(map(str,input().split()))
    key={"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5,
         "SIX":6, "SVN":7, "EGT":8, "NIN":9}

    sorted_arr=sorted(arr,key=key.get)
    print(test_case)
    for i in range(len(arr)):
        print(sorted_arr[i],end=" ")
    print()