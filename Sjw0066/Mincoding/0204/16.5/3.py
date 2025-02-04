arr=[]
lst1=list(map(int,input().split()))

arr.append(lst1[:3])
arr.append(lst1[3:])
index_min=[0,0]
index_max=[0,0]
def min_index():
    global index_min
    
    min_num= 1e21
    for i in range(2):
        for j in range(3):
            if arr[i][j] < min_num:
                min_num=arr[i][j]
                index_min=[i,j] 
def max_index():
    global index_max
    

    max_num= -1e21
    for i in range(2):
        for j in range(3):
            if arr[i][j] > max_num:
                max_num=arr[i][j]
                index_max=[i,j]
min_index()
max_index()
print(f'({index_max[0]},{index_max[1]})')   
print(f'({index_min[0]},{index_min[1]})')   