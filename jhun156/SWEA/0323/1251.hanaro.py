import sys
sys.stdin = open("input.txt","r")


def union(a,b,index):

    global cnt,total
    A,B = parent(a),parent(b)
    if A == B:
        return

    cnt += 1
    total += arr[index][2]
    group[B] = A


def parent(n):

    if group[n] != n:
        group[n] = parent(group[n])

    return group[n]


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    x_lst = list(map(int,input().split()))
    y_lst = list(map(int,input().split()))
    E = float(input())
    xy_lst = []
    for i in range(N):
        xy_lst.append((y_lst[i],x_lst[i]))

    arr = []
    for i in range(N):
        for j in range(i+1,N):
            arr.append((i,j,(xy_lst[i][0] - xy_lst[j][0]) ** 2 + (xy_lst[i][1] - xy_lst[j][1]) ** 2))

    group = [i for i in range(N+1)]
    arr.sort(key = lambda x:x[2])
    cnt = 0
    total = 0
    for i in range(len(arr)):
        if cnt == N:
            break
        union(arr[i][0],arr[i][1],i)

    total *= E
    ans = round(total)
    print(f"#{tc} {ans}")