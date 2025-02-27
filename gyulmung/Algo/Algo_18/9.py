arr =  [[15, 18, 17],
        [4, 6, 9], 
        [10, 1, 3], 
        [7, 8, 9], 
        [15, 2, 6]]

family = list(map(int, input().split()))

def Find_members(floor):
    for i in range(3):
        if arr[floor][i] == family[i]:
            return 5 - floor

for i in range(5):
    if arr[i][0] == family[0]:
        Floor = Find_members(i)
print(f'{Floor}층')