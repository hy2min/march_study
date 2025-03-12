# 최소신장트리 (길에 비용 정해져있을때 최소 비용 구하기)
# nlogn 정도 됨 ㅇㅇ
'''
5
8
A B 9
A C 3
A E 7
B C 14
B D 11
C D 1
C E 5
A D 20
'''
N=int(input())
M=int(input())

lst=[list(input().split()) for _ in range(M)]
sort_lst=sorted(lst,key=lambda x:int(x[2]))

def findboss(member):

    if not arr[ord(member)]:
        return member

    ret= findboss(arr[ord(member)])
    arr[ord(member)] = ret
    return ret

def union(a,b,i):
    global arr,cnt,total_cost
    a_boss,b_boss=findboss(a),findboss(b)
    if a_boss==b_boss:
        return
    total_cost+=int(sort_lst[i][2])
    cnt+=1
    arr[ord(b_boss)] = a_boss

arr=[0]*200
total_cost=0
cnt=0

for i in range(M):
    if cnt==N-1:
        print(total_cost)
        break
    union(sort_lst[i][0],sort_lst[i][1],i)


