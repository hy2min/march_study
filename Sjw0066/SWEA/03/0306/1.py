T=int(input())

for tc in range(1,T+1):
    N,str1=map(str,input().split())
    answer=''
    for i in str1:
        temp=int(i,16)
        binary_temp=str(bin(temp)[2:])

        if binary_temp[0] == 1:
            answer += '0'
            answer += binary_temp
        else:
            answer += binary_temp
    print(answer)