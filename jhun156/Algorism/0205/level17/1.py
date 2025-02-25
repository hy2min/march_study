arr = ['M','T','K','C']
a = input()

def isExist(a):
    for i in range(4):
        if arr[i] == a:
            return 1
    return 0

result = isExist(a)
if result == 1:
    print("발견")
else:
    print("미발견")