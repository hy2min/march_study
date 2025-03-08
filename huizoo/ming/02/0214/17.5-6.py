pw = [3,7,4,9]
input1 = list(map(int, input().split()))
def isSame(arr):
    if arr == pw:
        return 'pass'
    return 'fail'

print(isSame(input1))