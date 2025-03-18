# N=int(input())
# lst=[0,7,-3,-5,-4,-2,6,5,-9,1,0]
# ans=[0]*N
# ans[1]=lst[1]
#
# for i in range(2,N):
#     if i%2==0:#         ans[i]=max(ans[i-1],ans[i-2],ans[i//2])+lst[i]
#     else:
#         ans[i] = max(ans[i - 1], ans[i - 2])+lst[i]
#
# print(ans[N-1])
#
# arr=[
#     [0,5,3,6,8],
#     [1,4,2,9,1],
#     [6,9,1,7,7],
#     [8,5,4,1,0],
# ]
# ans=[[0]*5 for _ in range(4)]
#
# for i in range(4):
#     for j in range(5):
#         if i<1:
#             ans[i][j] = ans[i][j-1]+arr[i][j]
#         else:
#             ans[i][j]=min(ans[i-1][j],ans[i][j-1])+arr[i][j]
#
# print(ans[3][4])
# arr=[0,0,1,0]
# arr=[1,0,1,1]
#
# N=len(arr)
# answer=0
# for i in range(N):
#     answer+=arr[i]*2**(N-i-1)
# print(answer)


# bottom up  점화식 통해 작은부분 해결하면서 큰 문제 해결

# greedy는 뒷일 생각 x

# bottom up 은 뒷일 생각함 ㅇㅇ
# data를 모두 고려하고 선택을 1개한뒤 바뀐 data를 이용함

# knap sack 이 대표적 알고리즘
# 배낭문제라고 많이함
'''
한 달 후면 국가의 부름을 받게 되는 정싸피는 여행을 가려고 한다.
세상과의 단절을 슬퍼하며 최대한 즐기기 위한 여행이기 때문에,
가지고 다닐 배낭 또한 최대한 가치 있게 싸려고 한다.
정싸피가 여행에 필요하다고 생각하는 N개의 물건이 있다.

각 물건은 무게 W와 가치 V를 가지는데, 해당 물건을 배낭에 넣어서 가면 정싸피가 V만큼 즐길 수 있다.
아직 행군을 해본 적이 없는 정싸피는 최대 K만큼의 무게만을 넣을 수 있는 배낭만 들고 다닐 수 있다.
정싸피가 최대한 즐거운 여행을 하기 위해 배낭에 넣을 수 있는 물건들의 가치의 최댓값을 알려주자.

입력
첫 줄에 물품의 수 N(1 ≤ N ≤ 100)과 정싸피가 버틸 수 있는 무게 K(1 ≤ K ≤ 100,000)가 주어진다.
두 번째 줄부터 N개의 줄에 거쳐 각 물건의 무게 W(1 ≤ W ≤ 100,000)와
해당 물건의 가치 V(0 ≤ V ≤ 1,000)가 주어진다.
입력으로 주어지는 모든 수는 정수이며 제한시간은 2초 이다.

출력
한 줄에 배낭에 넣을 수 있는 물건들의 가치합의 최댓값을 출력한다.

4 7
6 13
4 8
3 6
5 12

출력
14

'''
# N,K = map(int,input().split())
# ans=[[0]*(K+1) for _ in range(N+1)]
# lst=[[0,0]]
# for i in range(1,N+1):
#     W,V=map(int,input().split())
#     lst.append([W,V])
#
# for i in range(1,N+1):
#     W,V=lst[i]
#     for j in range(1,K+1):
#         if j<W:
#             ans[i][j]=ans[i-1][j]
#         else:
#             ans[i][j]=max(ans[i-1][j],V+ans[i-1][j-W])
#
# print(ans[N][K])

'''
7 1 10 원짜리 동전이 있다
14원 거슬러 줄때 최소동전의 개수?

n - 동전의 종류 개수
k - 거슬러줄 돈
사용할 동전입력받기

입력예제
3 14
7
1
10

출력결과
2
'''
#
# n,k=map(int,input().split())
# lst=[0]
# for i in range(n):
#     lst.append(int(input()))
# arr=[[21e8]*(k+1) for _ in range(n+1)]
#
# for i in range(1,n+1):
#     coin=lst[i]
#     for j in range(1,k+1):
#         if j%coin==0:
#             arr[i][j] = j//coin
#         else:
#             if j//coin==0:
#                 arr[i][j] = arr[i-1][j]
#             else:
#                 arr[i][j] = min(arr[i-1][j],j//coin+arr[i][j-j%coin])
#
# print(arr[n][k])

# 일차원 배열


# n,k=map(int,input().split())
# coin=[]
# for i in range(n):
#     don=int(input())
#     coin.append(don)
# coin.sort()
# arr=[1001]*(k+1)
# arr[0]=0
# for i in range(n):
#     start=coin[i]
#     for j in range(start,k+1):
#         arr[j]=min(arr[j],arr[j-start]+1)
# print(arr[k])

# 1.최장 공통 부분 문자열
# 2.최장 공통 부분 수열
# 3.최장 증가 부분 수열

# 1. 연속된 문자열 중의 길이가 가장 길때 그 길이를 출력하는것
#
# str1=input()
# str2=input()
#
# arr=[[0]*(len(str2)+1) for _ in range(len(str1)+1) ]
# Max=-21e8
#
# for i in range(1,len(str1)+1):
#     for j in range(1,len(str2)+1):
#         if str1[i-1] == str2[j-1]:
#             arr[i][j] = arr[i-1][j-1]+1
#             if Max<arr[i][j]:
#                 Max=arr[i][j]
#                 max_y=i
#                 max_x=j
#         else:
#             arr[i][j] = 0
#
#
# for i in range(Max):
#     print(str2[max_x-Max+i],end="")

# 2. 최장 공통 부분 순열
# str1=input()
# str2=input()
#
# arr=[[0]*(len(str2)+1) for _ in range(len(str1)+1) ]
# Max=-21e8
#
# for i in range(1,len(str1)+1):
#     for j in range(1,len(str2)+1):
#         if str1[i-1] == str2[j-1]:
#             arr[i][j] = arr[i-1][j-1]+1
#             if Max<arr[i][j]:
#                 Max=arr[i][j]
#                 max_y=i
#                 max_x=j
#         else:
#             arr[i][j] = max(arr[i-1][j],arr[i][j-1])
#
# lcs = []
# i, j = len(str1), len(str2)
# while i > 0 and j > 0:
#     if str1[i - 1] == str2[j - 1]:
#         lcs.append(str1[i - 1])  # 일치하는 문자 추가
#         i -= 1
#         j -= 1
#     elif arr[i - 1][j] >= arr[i][j - 1]:
#         i -= 1  # 왼쪽으로 이동
#     else:
#         j -= 1  # 위로 이동
#
# # 최장 공통 부분 수열을 뒤집어서 출력
# print(''.join(reversed(lcs)))

# 3 최장 증가 부분 수열

# 10 20 10 30 20 50
# segment tree 자료 구조 사용하면 nlogn으로도 가능
# segment tree, hash b형에서 중요함 ㅇㅇ
N=int(input())
arr=list(map(int,input().split()))

result=[1]*N
for i in range(N):
    std=arr[i]
    for j in range(i):
        val=arr[j]

        if std>val:
            result[i]=max(result[j]+1,result[i])

print(max(result))









