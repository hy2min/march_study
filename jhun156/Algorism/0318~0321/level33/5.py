# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
size = list(map(int,input().split()))
arr = [i for i in range(N)]
M = int(input())

def union(a,b):

    A,B = find(a),find(b)

    if A < B:
        arr[B] = A
    else:
        arr[A] = B

def find(a):

    if arr[a] == a:
        return a

    ret = find(arr[a])
    arr[a] = ret

    return ret

def Sum(num):

    ret = 0
    for i in range(N):
        if arr[i] == num:
            ret += size[i]

    return ret

def zero(num):

    for i in range(N):
        if arr[i] == num:
            size[i] = 0

for _ in range(M):
    command,a,b = input().split()
    if command == 'alliance':
        n1 = ord(a) - 65
        n2 = ord(b) - 65
        union(n1,n2)

    elif command == 'war':

        n1 = ord(a) - 65
        n2 = ord(b) - 65
        people1 = Sum(arr[n1])
        people2 = Sum(arr[n2])

        if people1 < people2:
            zero(arr[n1])
        elif people2 < people1:
            zero(arr[n2])

cnt = 0
for i in range(N):
    if size[i] != 0:
        cnt += 1

print(cnt)