arr=[[[2,4], [1, 5]],
     [[2, 3], [3, 6]],
     [[7, 3], [1, 5]]]

num = int(input())
Max = -1e8
Min = 1e8

def abc(lev):
    global Max, Min
    if lev == 2:
        return

    for i in range(2):
        Max = max(Max, arr[num][lev][i])
        Min = min(Min, arr[num][lev][i])
    abc(lev + 1)

abc(0)
print(f'MAX={Max}\nMIN={Min}')