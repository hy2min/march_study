arr = ['M','T','K','C']
a = input()
def isExist(char):
    for i in range(4):
        if arr[i] == a:
            return '발견'
    return '미발견'

print(isExist(a))