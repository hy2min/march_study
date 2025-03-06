T = int(input())
for tc in range(1, T+1) : 
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = 1
    for row in arr : 
        if len(set(row)) != 9 : 
            flag = 0
    for row in list(zip(*arr)) : 
        if len(set(row)) != 9 : 
            flag = 0
    
    for i in range(0, 9, 3) : 
        for j in range(0, 9, 3) : 
            dat = [0]*10
            for y in range(3) : 
                for x in range(3) : 
                    dat[arr[i+y][i+x]] += 1
            if dat.count(1) != 9 : 
                flag = 0
    if flag : 
        print(f'#{tc} 1')
    else : 
        print(f'#{tc} 0')


# T = int(input())
# for tc in range(1, T+1) :
#     arr = [list(map(int, input().split())) for _ in range(9)]
#     flag = False
#     dat = [0]*10
#     n = 1
#     for y in range(9) :
#         for x in range(9) :
#             dat[arr[y][x]] += 1
#         if dat.count(n) != 9 :
#             flag = True
#         n += 1

#     arr = list(zip(*arr))
#     for y in range(9):
#         for x in range(9):
#             dat[arr[y][x]] += 1
#         if dat.count(n) != 9 :
#             flag = True
#         n += 1

#     for i in range(0, 9, 3) :
#         for j in range(0, 9, 3) :
#             for y in range(3) :
#                 for x in range(3) :
#                     dat[arr[i+y][j+x]] += 1
#             if dat.count(n) != 9 :
#                 flag = True
#             n += 1

#     if flag :
#         print(f'#{tc} 0')
#     else :
#         print(f'#{tc} 1')