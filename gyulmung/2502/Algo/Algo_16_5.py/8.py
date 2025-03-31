arr =[['A', '7', '9', 'T', 'K', 'Q'], ['M', 'I', 'N', 'C', 'O', 'D']]
st1, st2 = map(str, input().split())

# def isExist(st):
#     for i in arr:
#         for j in i:
#             if st == j:
#                 return f'{st} : 존재'
#             else:
#                 return f'{st} : 없음'

def isExist(st):
    for i in range(2):
        for j in range(6):
            if st == arr[i][j]:
                return f'{st} : 존재'
    return f'{st} : 없음'

print(isExist(st1))
print(isExist(st2))