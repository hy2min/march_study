arr=[list(input()) for _ in range(4)]
ay=0
ax=0
by=0
bx=0
for i in range(4):
    for j in range(3):
        if arr[i][j] == 'A':
            ay=i
            ax=j
        if arr[i][j] == 'B':
            by=i
            bx=j

answer=abs((ay+ax)-(by+bx))
print(answer)



