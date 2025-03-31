arr = ['M', 'T', 'K', 'C']
st = input()

def isExist():
    for i in range(4):
        if st == arr[i]:
            return '발견'
            
    return '미발견'

print(isExist())