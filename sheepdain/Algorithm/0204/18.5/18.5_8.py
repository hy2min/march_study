a,b,c=input(),input(),input()
arr=a+b+c
def isFind(arr):
    L_arr=len(arr)
    for i in range(L_arr):
        for j in range(i+1,L_arr):
            if arr[i]==arr[j]:
                return print('No')
    return print('Perfect')
isFind(arr)