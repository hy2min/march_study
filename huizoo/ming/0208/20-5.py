arr = list(input())
def arr_print(lst) : 
    print(lst[0], end = '')
    if len(lst) > 1 : 
        arr_print(lst[1:])
    if len(lst) == 1 : 
        print()
    print(lst[0], end = '')

arr_print(arr)