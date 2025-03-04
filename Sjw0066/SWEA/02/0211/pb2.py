T= int(input())

for tc in range(1, T + 1):
    str1=input()
    str2=input()
    answer=0

    for i in range(len(str2)-len(str1)+1):
        cnt=0
        for j in range(len(str1)):
            if str1[j] == str2[i+j]:
                cnt+=1
        if cnt==len(str1):
            answer=1

    
    print(f'#{tc} {answer}')