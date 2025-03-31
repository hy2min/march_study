import sys
sys.stdin = open("input.txt","r")

def union(a,b):

    A,B = parent(a),parent(b)
    if A == B:
        return

    if A < B:
        group[B] = A
    else:
        group[A] = B

def parent(num):

    if group[num] == num:
        return num
    group[num] = parent(group[num])

    return group[num]

T = int(input())
for tc in range(1,T+1):
    N,M = map(int,input().split())
    wish_list = list(map(int,input().split()))
    group = [i for i in range(N+1)]
    # 나중에 그룹에서 0번 인덱스 제거할 예정
    for i in range(0,M*2,2):
        union(wish_list[i],wish_list[i+1])

    for i in range(N+1):
        parent(group[i])
    ans = set(group[1:])
    print(f"#{tc} {len(ans)}")