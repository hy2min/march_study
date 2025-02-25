# import sys
# sys.stdin = open("input.txt","r")

T= int(input())
for tc in range(1,T+1):
    str1 = input()
    str2 = input()
    str_dict = {}
    for i in range(len(str1)):
        str_dict[str1[i]] = str2.count(str1[i])

    ans = 0
    for key,value in str_dict.items():
        if value == max(str_dict.values()):
           ans = value

    print(f"#{tc} {ans}")