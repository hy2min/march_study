T=int(input())

for tc in range(1,T+1):
    N,str1=map(str,input().split())
    hex_num='0123456789ABCDEF'
    answer=''
    for i in range(len(str1)):
        for j in range(16):
            if hex_num[j]==str1[i]:
                n=j
                binary_temp = ''
                while n:

                    binary_temp=str(n%2)+binary_temp
                    n=n//2
                answer+=binary_temp.zfill(4)
    print(f'#{tc} {answer}')



