def main():
    arr = [[0] * 3 for _ in range(3)]
    result = magic(arr)
    output(result)

def magic(lst):
    num = 1
    start_num = 0
    for i in range(3):
        for j in range(start_num,3):
            lst[i][j] = num
            num += 1
        start_num += 1
    return lst
    
def output(lst):
    for i in range(3):
        for j in range(3):
            if lst[i][j] == 0:
                print(' ',end='')
            else:
                print(lst[i][j],end='')
        print()
    
main()