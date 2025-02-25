a = input()
b = input()

def isSame(str1,str2):
    if str1 == str2:
        return 1
    else:
        return 0
    
ans = isSame(a,b)
if ans == 1:
    print("동명")
else:
    print("남남")