

def main():
    arr = [[0]*3 for _ in range(3)]
    arr1 = magic(arr)
    output(arr1)



def magic(arr) :
    num= 1
    for i in range(3) :
        for j in range(3-i) :
            arr[i][j] = num
            num +=1
    return arr


def output(arr1) :
    for i in range(3) :
        print(" " * i, end="")
        for j in range(3):
            if arr1[i][j] != 0:
                print(arr1[i][j], end="")
        print()

main()