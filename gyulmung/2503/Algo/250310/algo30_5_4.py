import sys
sys.stdin = open('input.txt', 'r')

str1 = input()
str2 = input()
str3 = input()

# # 1 길이가 긴것 먼저 확인하기
# if len(str1) > len(str2):
#     if len(str1) > len(str3):
#         if len(str2) > len(str3):
#             a, b, c = str1, str2, str3
#         else:
#             a, b, c = str1, str3, str2
#     else:
#         a, b, c = str3, str1, str2
# else:
#     if len(str2) > len(str3):
#         if len(str3) > len(str1):
#             a, b, c = str2, str3, str1
#         else:
#             a, b, c = str2, str1, str3
#     else:
#         a, b, c = str3, str2, str1

s1 = int(str1)
s2 = int(str2)
s3 = int(str3)

if s1 > s2:
    if s1 > s3:
        if s2 > s3:
            print(s1)
        else:
            print(s1)
    else:
        print(s3)
else:
    if s2 > s3:
        if s3 > s1:
            print(s2)
        else:
            print(s2)
    else:
        print(s3)