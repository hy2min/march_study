# import sys
# sys.stdin = open("input.txt","r")

arr = [0] * 200
arr[ord('A')] = 1
arr[ord('B')] = 'A'
arr[ord('C')] = 'A'

arr[ord('D')] = 1
arr[ord('E')] = 'D'
arr[ord('F')] = 'D'

arr[ord('H')] = 1
arr[ord('G')] = 'H'

arr[ord('I')] = 1
arr[ord('J')] = 'I'

def union(a,b):

    A,B = find(a),find(b)
    if A == B:
        return 0

    arr[ord(B)] = A
    return 1

def find(num):

    if arr[ord(num)] == 1:
        return num

    ret = find(arr[ord(num)])
    arr[ord(num)] = ret
    return ret


ans = 4
N = int(input())
for _ in range(N):
    a,b = input().split()
    tmp = union(a,b)
    if tmp:
        ans -= 1

print(f"{ans}개")