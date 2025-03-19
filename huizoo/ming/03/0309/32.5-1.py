arr = [
    'ABCD',
    'ABCE',
    'AGEH',
    'EIEI',
    'FEQE',
    'ABAD',
]
st = input()
arr2 = [0]*6
for i in range(4):
    if st[i] == '?':
        for j in range(6):
            arr2[j] += 1
    else:
        for j in range(6):
            if st[i] == arr[j][i]:
                arr2[j] += 1
print(arr2.count(4))