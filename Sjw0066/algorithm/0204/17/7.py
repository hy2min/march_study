arr1=[[0,0,1,0,0],[0,0,1,1,1]]
arr2=[[3,5,4,1,1],[3,5,2,5,6]]

flag=0
a=int(input())
for i in range(2):
    for j in range(5):
        if arr1[i][j] == 1 :
            if arr2[i][j] == a :
                flag=1

if flag ==1 :
    print(f'{a} 존재')
else:
    print(f'{a} 없음')
        