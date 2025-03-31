T= int(input())

for tc in range(1, T + 1):
    str1=input()
    str2=input()

    dat=[0]*100
    dict1={}
    for i in str1:
        dat[ord(i)] += 1
    
    for i in range(len(dat)):
        cnt=0
        for j in str2:
            if dat[i] and i == ord(j):
                cnt+=1
        if cnt:
            dict1.setdefault(chr(i),cnt)

           

    answer=max(dict1.values())
    print(f'#{tc} {answer}')