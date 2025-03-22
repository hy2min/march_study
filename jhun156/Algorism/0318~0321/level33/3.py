# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
a = 65
cnt = 0
lst = []
while cnt < N:
    lst.append(chr(a))
    a += 1
    cnt += 1

ans = 0
check = set()

def union(a,b):

    A,B = find(a),find(b)

    if A == B:
        return 1

    lst[ord(B)-65] = A

def find(num):

    if lst[num] == chr(num+65):
        return chr(num+65)

    ret = find(ord(lst[num])-65)
    lst[num] = ret
    return ret

for i in range(N):
    for j in range(i+1,N):
        if arr[i][j] == 1 and (i,j) not in check:
            check.add((i,j))
            ans = union(i,j)
            if ans:
                break
    if ans:
        break

if ans:
    print("cycle 발견")
else:
    print('미발견')