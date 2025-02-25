arr = [4,4,5,7,8,10,20,22,23,24]

def binary_search(key):
    st = 0
    ed = 9
    while True:
        mid = (st + ed) // 2
        if arr[mid] == key:
            return 1
        elif arr[mid] > key:
            ed = mid - 1
        elif arr[mid] < key:
            st = mid + 1
        if st > ed:
            return 0

a = int(input())
ans = binary_search(a)
if ans:
    print("O")
else:
    print("X")