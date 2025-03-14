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
arr=[0,0,1,0]
# arr=[1,0,1,1]

N=len(arr)
answer=0
for i in range(N):
    answer+=arr[i]*2**(N-i-1)
print(answer)





