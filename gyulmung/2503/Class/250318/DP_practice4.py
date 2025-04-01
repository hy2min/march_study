import sys
sys.stdin = open('input.txt', 'r')

s1="BABJYP"
s2="ABCBJY"

def LCS(s1, s2):
    len1, len2 = len(s1), len(s2)
    arr = [[0]*(len1 + 1) for _ in range(len2 + 1)]

    for i in range(1, len2 + 1):
        for j in range(1, len1 + 1):
            if s2[i-1] == s1[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])
    return arr[len1][len2]

ret = LCS(s1, s2)
print(ret)
