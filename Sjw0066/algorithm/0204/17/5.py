arr=[[3,5,9],[4,2,1],[5,1,5]]

lst1=list(map(int,input().split()))

def isExist(arr,lst1):
    for i in range(3) :
        
        for j in range(3):
            if lst1[i] in arr[j] :
                flag=1
        if flag==1:    
            print(f'{lst1[i]}:존재')                
        else:    
            print(f'{lst1[i]}:미발견')
        flag=0

isExist(arr,lst1)