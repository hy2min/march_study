# import sys
# sys.stdin = open("input.txt","r")

N = int(input())
arr = [0] * 200

def union(a,b):

    A = find_boss(a)
    B = find_boss(b)
    if A == B:
        return 1
    arr[ord(B)] = A


def find_boss(a):

    if arr[ord(a)] == 0:
        return a
    ret = find_boss(arr[ord(a)])
    arr[ord(a)] = ret
    return ret

for _ in range(N):
    a, b = input().split()
    ans = union(a,b)
    if ans:
        print("발견")
        break
else:
    print("미발견")
