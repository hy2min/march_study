a1 = ['A','B','C','D','E']
a2 = ['a','b','c','d','e']
a3 = ['0','1','2','3','4']
a4 = ['F','G','H','I','J']
a5 = ['f','g','h','i','j']
arr =[]
for alpha in zip(a1, a2, a3, a4, a5):
    arr.append(alpha)
    print(*alpha, sep = '')
for i in range(5):
    for j in range(5):
        print(arr[i][j],end='')