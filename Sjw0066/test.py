# str1=input()
# index=0
# for i in range(len(str1)-1,-1,-1):
#     cnt=0
#     for j in range(len(str1)):
#         if j>=i:
#             cnt+=1
#
#     for k in range(len(str1)-cnt,len(str1)):
#         print(str1[k],end="")
#     print()
T =int(input())
for tc in range(1,T+1):
    N ,M = map(int,input().split())
    lst1=list(map(int,input().split()))
    lst2=list(map(int,input().split()))

    long=[]
    short=[]
    if N>M :
        long=lst1
        short=lst2
    else:
        long=lst2
        short=lst1

    max_sum=-21e8
    for i in range(len(long)-len(short)+1):
        Sum = 0
        for j in range(len(short)):

            Sum+=long[i+j] * short[j]

        if Sum>max_sum:
            max_sum=Sum

    print(f'#{tc} {max_sum}')
