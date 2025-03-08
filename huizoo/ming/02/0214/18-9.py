arr = [
    [15,18,17],
    [4,6,9],
    [10,1,3],
    [7,8,9],
    [15,2,6],
]
arr2 = list(map(int, input().split()))

def isPattern():
    for i in range(5):
        if arr[i] == arr2:
            return 5-i
        
print(f'{isPattern()}층')

