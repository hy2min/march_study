arr=[['A','D','F'],['Q','W','E'],['Z','X','C']]
def main():
    str1=input()
    result=find(str1)
    
    print(result[0],end=",")
    print(result[1])
    
    

def find(str1):
    result=[]

    for i in range(len(arr)):
        for j in range(len(arr[i])) :
            if arr[i][j] == str1 :
                result.append(i)
                result.append(j)
    return result

main()