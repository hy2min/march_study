n = int(input())
arr = [3,7,4,1,9,4,6,2]
def kfc(lst , i) : 
    print(lst[i], end = ' ')
    if i > 0 : 
        kfc(lst, i-1)
        print(lst[i], end = ' ')

kfc(arr, n)