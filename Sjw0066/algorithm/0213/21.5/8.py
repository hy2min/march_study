def model_action(model,action):
    y=0
    x=0
    for i in range(5):
        for j in range(3):
            if model == arr[i][j]:
                y=i
                x=j

    if action == "UP":
        if y-1>=0:
            arr[y][x] ,arr[y-1][x] = arr[y-1][x],arr[y][x]
    if action == "DOWN":
        if y+1<=4:
            arr[y][x] ,arr[y+1][x] = arr[y+1][x],arr[y][x]
    if action == "RIGHT":
        if x+1<=2:
            arr[y][x] ,arr[y][x+1] = arr[y][x+1],arr[y][x]
    if action == "LEFT":
        if x-1>=0:
            arr[y][x] ,arr[y][x-1] = arr[y][x-1],arr[y][x]
arr=[
    ['_','_','_'],
    ['_','_','_'],
    ['A','T','K'],
    ['_','_','_'],
    ['_','_','_'],
]

for i in range(7):
    a,b=map(str,input().split())
    model_action(a,b)

for i in arr:
    for j in i:
        print(j,end="")
    print()