arr = [['G', 'K', 'T'], ['P', 'A', 'C']]
st1, st2 = map(str, input().split())

def isExist(count):
    if count == 2:
        print('대발견')
    elif count == 1:
        print('중발견')
    else:
        print('미발견')

count = 0
for i in range(2):
    for j in range(3):
        if st1 == arr[i][j]:
            count += 1
        elif st2 == arr[i][j]:
            count += 1
isExist(count)
