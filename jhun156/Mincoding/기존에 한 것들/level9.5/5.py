def Input():

    arr = [i for i in input().split()]
    lst = []
    count = 0

    for i in range(2):
        row = []
        for j in range(3):
            row.append(arr[count])
            count += 1
        lst.append(row)
    
    return lst

def findUpper(arr):

    count = 0

    for i in range(2):
        for j in range(3):
            if arr[i][j].isupper():
                count += 1
    print(f"대문자{count}개")

def findLower(arr):

    count = 0
    
    for i in range(2):
        for j in range(3):
            if arr[i][j].islower():
                count += 1
    print(f"소문자{count}개")

def main():
    
    lst = Input()
    findUpper(lst)
    findLower(lst)

main()

