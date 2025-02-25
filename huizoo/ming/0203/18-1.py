MAX_ID = 65536

arr = [[65000, 35, 42, 70],
       [70, 35, 65000, 1300],
       [65000, 30000, 38, 42],
       ]

dat = [0] * MAX_ID

for row in arr :
    for id in row : 
        dat[id] += 1

max_cnt = max(dat)
most_id = dat.index(max_cnt)
print(most_id)
