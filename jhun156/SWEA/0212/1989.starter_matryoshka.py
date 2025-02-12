# import sys
# sys.stdin = open("input.txt","r")

def matryoshka(str):
    a = len(str)
    for i in range(a//2):
        if str[i] != str[a-1-i]:
            return 0
    return 1

T = int(input())
for tc in range(1,T+1):
    string = input()
    ans = matryoshka(string)
    print(f"#{tc} {ans}")
