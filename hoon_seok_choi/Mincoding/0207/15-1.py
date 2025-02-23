a = input()
b = input()

arr1 = [*a]
arr2 = [*b]



cnt = 0

for i in range(len(a)) :
    if arr1[i] ==  arr2[i] :
        cnt += 1

if len(arr1) == cnt and len(arr2) == cnt :
    print("같음") 
else :
    print("다름")