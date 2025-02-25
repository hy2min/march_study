# a=[3,8,5,2,5,7,2,4]
#
# n=int(input())
#
# b=list(map(int,input().split()))
#
# cnt=0
# for i in range(len(b)):
#     cnt=0
#     for j in range(len(a)):
#         if b[j] == a[j] :
#             cnt+=1
#
#     print(b[i],cnt)

#이를 DirectAddressTable 을 사용하면 이를 수행할때 시간복잡도 단축가능

# a=[3,8,5,2,5,7,2,4]
#
# n=int(input())
#
# b=list(map(int,input().split()))
#
# bucket=[0]*10
#
# for i in range(len(a)):
#     bucket[a[i]] += 1
#
# for i in range(len(b)):
#     print(bucket[b[i]])

'''
문제
n개의 숫자 입력
어떤 숫자 몇개 입력인지 출력
'''

# n=int(input())
# lst1=list(map(int,input().split()))
#
# dat=[0]*10
#
# for i in lst1:
#     dat[i] +=1
#
# for i in range(len(dat)):
#     if dat[i] != 0:
#         print(f'{i} : {dat[i]} 개 있음')

'''
어떤 문자열 몇번 사용됨?
'''

# str1=input()
#
# bucket = [0]*200
#
# for i in str1:
#     bucket[ord(i)] += 1
#
# for i in range(len(bucket)):
#     if bucket[i] != 0:
#         print(f'{chr(i)} : {bucket[i]}개')

# dat 사용하여 정렬하기
#
# lst=list(map(int,input().split()))
#
# dat=[0]*10
#
# sort_lst=[0]*len(lst)
#
# for i in lst:
#     dat[i] += 1
#
# for i in range(1,10):
#     dat[i] = dat[i] + dat[i-1]
#
# for i in lst:
#     dat[i] -= 1
#     sort_lst[dat[i]] = i
#
# print(sort_lst)

# 정렬 부분 다시 보기

# #리스트
# lst=[[4,5,2,6,7,3,1],
#     [2,9,9,6,1,6,7]]
#
# max_sum=-21e8
# sum=0
#
# for i in range(len(lst)):
#     for j in range(len(lst[i])-2):
#         sum=0
#         for k in range(3):
#             sum+=lst[i][j+k]
#         if sum>max_sum:
#             max_sum=sum
#
# print(max_sum)

'''
1 2 3 4 5 
2 4 2 1 3
3 4 5 2 5    

3 4 5 라는 패턴이 어느 좌표에 있는지 찾기!!

정답은: 
0,2
2,1

'''
# arr=[[1,2,3,4,5],[2,4,2,1,3],[3,4,5,2,5]]
# flag=0
# for i in range(3):
#     for j in range(3):
#         if arr[i][j:j+3] == [3,4,5]:
#             flag=1
#             print(f'{i},{j}')
# if flag==0:
#     print('패턴없음')

'''
1 5 4 2
1 3 4 2
3 5 3 2
2 6 4 1

* * *
* * * 
이 모양으로 땅을 가질 수 있다. 합이 최댓값이 되게하는 왼쪽위 점을 구해라 
'''
lst=[[1 ,5 ,4 ,2],
    [1 ,3 ,4 ,2],
    [3 ,5 ,3 ,2],
    [2 ,6 ,4 ,1]]
def getMax(y,x):
    Sum=0
    for i in range(2):
        for j in range(3):
            Sum+=lst[y+i][x+j]

    return Sum

max_sum=-21e8


for i in range(3):
    for j in range(2):
        ret=getMax(i,j)
        if ret>max_sum:
            max_sum=ret

print(max_sum)
