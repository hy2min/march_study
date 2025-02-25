arr = [
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
    [0,0,0,0],
]

check_list = []
for i in range(3):
    row = list(input().split())
    check_list.extend(row)

def Fill_block(GB,num):
    if GB == "G":
        for i in range(4):
            if arr[num][i] == 1:
                continue
            else:
                arr[num][i] = 1
    else:
        for i in range(4):
            for i in range(4):
                if arr[i][num] == 1:
                    continue
                else:
                    arr[i][num] = 1

for i in range(0,6,2):
    Fill_block(check_list[i],int(check_list[i+1]))

for i in range(4):
    print(*arr[i])