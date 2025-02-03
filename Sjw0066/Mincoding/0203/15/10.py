def main():
    
    arr=[[0]*10 for _ in range(3)]

    for i in range(3):
        str1=list(input())
        for j in range(len(str1)):
            arr[i][j] = str1[j]

    CountLine(arr)

def CountLine(arr):
    for i in arr:
        print(f'{len(list(filter(bool,i)))}={"".join(list(filter(bool,i)))}')
main()