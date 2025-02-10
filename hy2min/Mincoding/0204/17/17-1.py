arr = ['M','T','K','C']
s = input()

def isExist():
    if s in arr:
        return "발견"
    else:
        return "미발견"

print(isExist())