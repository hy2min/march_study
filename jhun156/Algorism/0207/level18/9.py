apart = [
    [15,18,17],
    [4,6,9],
    [10,1,3],
    [7,8,9],
    [15,2,6],
]

family = [i for i in map(int,input().split())]

def isPattern(num):
    if apart[num] == family:
        return 1
    else:
        return 0

for i in range(5):
    ans = isPattern(i)
    if ans == 1:
        print(f"{5-i}층")
