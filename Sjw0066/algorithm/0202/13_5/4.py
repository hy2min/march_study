arr=[[3,4,1,6],[3,5,3,6],list(map(int,input().split())),[5,4,6,0]]

MAX=0
MIN=1e21
max_index=[0,0]
min_index=[0,0]



for i in range(len(arr)):
    for j in range(len(arr[i])) :
        if arr[i][j]>MAX:
            MAX=arr[i][j]
            max_index[0]=(i)
            max_index[1]=(j)
        if arr[i][j]<MIN:
            MIN=arr[i][j]
            min_index[0]=(i)
            min_index[1]=(j)
            
print(f'MAX={MAX}({max_index[0]},{max_index[1]})')
print(f'MIN={MIN}({min_index[0]},{min_index[1]})')
