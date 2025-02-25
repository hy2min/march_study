def isPattern(i):
        if sorted(apartments[i]) == sorted(family):
            return 1
        else:
            return 0

apartments = [
    [15,18,17],
    [4,6,9],
    [10,1,3],
    [7,8,9],
    [15,2,6],
]
family = list(map(int, input().split()))

for i in range(5):
    if isPattern(i):
        print(f'{5-i}층')
