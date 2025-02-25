arr = [['G', 'K', 'T'], 
       ['P', 'A', 'C']]


arr2 = list(map(str, input().split()))
cnt =0

for i in range(2) :
    for j in range(2) :
        if arr2[i] in arr[j] :
            cnt +=1

if cnt == 2 :
    print('대발견')
elif cnt == 1 :
    print('중발견')
elif cnt == 0 :
    print('미발견')