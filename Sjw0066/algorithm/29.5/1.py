arr=[3,1,2,1,3,2,1,2,1]

def abc(index,level):

    if index>=len(arr)-1:
        print('도착',end=" ")
        return

    if level==0:
        print('시작',end=" ")

    print(arr[index],end=" ")
    abc(index+arr[index],level+1)
    print(arr[index],end=" ")
    if level==0:
        print('시작',end=" ")

n=int(input())

abc(n-1,0)