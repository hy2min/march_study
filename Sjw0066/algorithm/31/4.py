arr=[list(input()) for _ in range(5)]
flag=0
for i in range(5):
    arr[i][1],arr[i][3] = arr[i][3],arr[i][1]

for i in arr:
    if i==['M','A','P','O','M']:
        flag=1

if flag:
    print('yes')
else:
    print('no')