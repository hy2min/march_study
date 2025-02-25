# import sys
# sys.stdin = open("input.txt","r")

T = int(input())
for tc in range(1,T+1):
    ans = 0
    str1 = input()
    str2 = input()
    for i in range(len(str2)-len(str1)+1):
        if str1 == str2[i:i+len(str1)]:
            ans = 1
            break

    print(f"#{tc} {ans}")
