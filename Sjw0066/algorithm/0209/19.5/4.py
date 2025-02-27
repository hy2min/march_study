arr=[[0]*4 for _ in range(4)]

def change_color(input1,input2):
    global arr
    for i in range(4):
        for j in range(4):
            if input1 == 'G':
                arr[int(input2)][j] = 1
            else:
                arr[j][int(input2)] = 1 

for i in range(3):
    input1,input2=map(str,input().split())
    change_color(input1,input2)

for i in range(4):
    for j in range(4):
        print(arr[i][j],end=" ")
    print()