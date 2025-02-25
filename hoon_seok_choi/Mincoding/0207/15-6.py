a = input()

arr = [*a]

cnt = 0
for i in range(len(a)-1) :
    if arr[i].isupper() : 
        if arr[i+1].islower() :
            cnt +=1
    else : 
        if  arr[i+1].isupper() :
            cnt +=1

if cnt == len(a) -1 :
    print("개구리문장")
else :
    print("일반문장")