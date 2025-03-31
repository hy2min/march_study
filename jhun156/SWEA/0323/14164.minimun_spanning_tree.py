# import sys
# sys.stdin = open("input.txt","r")

def union(a,b,index):

    global ans,cnt
    A,B = boss(a),boss(b)
    if A == B:
        return

    ans += arr[index][2]
    cnt += 1

    if A < B:
        parent[B] = A
    else:
        parent[A] = B

def boss(num):

    if parent[num] != num:
        parent[num] = boss(parent[num])
    return parent[num]


T = int(input())
for tc in range(1,T+1):
    V, E = map(int,input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]
    arr.sort(key=lambda x: x[2])
    parent = [i for i in range(V+1)]
    ans = 0
    cnt = 0
    for i in range(E):
        if cnt == V:
            print(f"#{tc} {ans}")
            break
        union(arr[i][0],arr[i][1],i)