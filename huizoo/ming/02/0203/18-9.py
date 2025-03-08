apart = [
    [15, 18, 17],
    [4, 6, 9],
    [10, 1, 3],
    [7, 8, 9],
    [15, 2, 6],
]
family = list(map(int, input().split()))

def isPattern(apart_list, input_list) : 
    for i in range(5) :
        if apart_list[i] == input_list : 
            return 5-i

floor = isPattern(apart, family)
print(f'{floor}층')
