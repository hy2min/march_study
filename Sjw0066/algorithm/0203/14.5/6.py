def main():
    arr=[[0]*3 for _ in range(3)]
    
    result=magic(arr)
    output(result)


def magic(arr):
    cnt=1
    for i in range(3):
        for j in range(i,3):
            arr[i][j]=cnt
            cnt+=1

    return arr

def output(result):
    for i in range(3):
        for j in range(3):
            if result[i][j] == 0:
                print(" ",end="")
            else:
                print(result[i][j],end="")
        print()
main()