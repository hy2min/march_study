arr=[['F','R','Q','W','T'],['G','A','S','Y','Q'],['A','S','A','D','B']]

int1=int(input())

for i in range(3):
    for j in range(5):
        if j == int1 :
            print(arr[i][j],end="")