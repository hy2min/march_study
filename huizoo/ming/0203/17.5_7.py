leveltable = [[10, 20],
              [30, 60],
              [100, 150],
              [200, 300],
              ]

kcals = list(map(int, input().split()))

for i in range(4) : 
    cnt = 0
    for kcal in kcals : 
        if leveltable[i][0] <= kcal <= leveltable[i][1] : 
            cnt += 1
    print(f'lev{i}:{cnt}')