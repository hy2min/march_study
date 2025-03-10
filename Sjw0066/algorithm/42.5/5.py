food=list(map(int,input().split()))
turn=int(input())
Max=-21e8
eagle=[
    [0,1,2],
    [3,4,5],
    [1,2,3,4],
]
used=[0]*3

def eat(lst):
    

def dfs(level,Sum,lst):
    global Max

    if level == turn :
        if Max<Sum:
            Max=Sum
        return

    temp=lst[:]


