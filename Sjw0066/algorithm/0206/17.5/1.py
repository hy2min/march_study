arr=[3,4,1,1,2,6,8,7,8,9,10]


def getSum(index):
    sum_by_index=0
    for i in range(index,index+5):
        
        sum_by_index+=arr[i]
    print(sum_by_index)
    
startIndex=int(input())

getSum(startIndex)