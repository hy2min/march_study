arr = [
    ['G','K','T'],
    ['P','A','C'],
]

def isExist():
    extened_arr = [j for i in arr for j in i]
    str1, str2 = input().split()

    if str1 in extened_arr and str2 in extened_arr:
        print("대발견")
    elif str1 in extened_arr or str2 in extened_arr:
        print("중발견")
    else:
        print("미발견")

isExist()