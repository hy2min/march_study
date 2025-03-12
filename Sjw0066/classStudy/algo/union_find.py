# # union_find 자료구조
# # 각각의 독립된 데이터를 그룹화 시켜서 관리하고 싶을때 사용
# # 그래프의 사이클 파악,dfs 처럼 사용가능
#
# # ABCDEF라는 데이터가 있을때의 그룹화
# arr=[0]*200
#
# def union(a,b):
#     global arr
#
#     bossA,bossB=findboss(a),findboss(b)
#
#     if bossA==bossB:
#         return
#
#     arr[ord(bossB)]=bossA
#
# def findboss(member):
#     global arr
#
#     if arr[ord(member)] == 0:
#         return member
#
#     ret = findboss(arr[ord(member)])
#     arr[ord(member)] = ret
#     return ret
#
# union('A','B')
# union('D','E')
# union('B','E')
# union('B','D')
# union('E','F')
#
# y,x=input().split()
# if findboss(y)==findboss(x):
#     print('같은그룹')
# else: print('다른그룹')
#

# 정점 , 간선, 연결 주어질시 사이클 발생여부
#  5 5 A B ,B C ,D E ,A D ,C D 이케 주어짐
arr=[0]*100
N,M=map(int,input().split())
flag=0
def union(a,b):
    global arr,flag

    bossA,bossB=findboss(a),findboss(b)

    if bossA==bossB:
        flag=1
        return

    arr[ord(bossB)]=bossA

def findboss(member):
    global arr

    if arr[ord(member)] == 0:
        return member

    ret = findboss(arr[ord(member)])
    arr[ord(member)]=ret
    return ret

for i in range(M):
    a1,b1=map(str,input().split())
    union(a1,b1)

if flag:
    print('간선있음')
else:
    print('간선없음')





















