# import sys
# sys.stdin = open("input.txt","r")

arr1 = input()
arr2 = input()
if len(arr1) > len(arr2):
    arr1,arr2 = arr2,arr1
# 항상 가장 긴 문장은 arr2
n = len(arr1)
m = len(arr2)
ans = ''

def find(string):
    N = len(string)
    for i in range(m-N+1):
        if arr2[i:i+N] == string:
            return string
    return ''

for i in range(n,0,-1):
    for j in range(n-i+1):
        tmp = find(arr1[j:j+i])
        if len(tmp) != 0 and len(tmp) > len(ans):
            ans = tmp
            break

print(ans)